"""
Check for broken internal and external links across the site.
Uses the Flask test client for internal links and requests for external ones.
"""

import sys
import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import run_app  # noqa: E402

EXTERNAL_TIMEOUT = 10
SKIP_EXTERNAL = {"mailto:", "tel:"}

# Some hosts block automated requests — treat as warnings not failures
FLAKY_HOSTS = {"linkedin.com", "facebook.com"}


def get_all_routes(app):
    routes = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and "<" not in rule.rule:
            routes.append(rule.rule)
    return sorted(routes)


def get_links_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for tag in soup.find_all("a", href=True):
        href = tag["href"]
        if any(href.startswith(s) for s in SKIP_EXTERNAL):
            continue
        links.append(href)
    return links


def check_links():
    app = run_app()
    client = app.test_client()

    broken = []
    warnings = []

    routes = get_all_routes(app)
    print(f"Found {len(routes)} routes\n")

    # Crawl all pages and collect links
    all_internal = set(routes)
    external_links = {}  # url -> found on page

    for route in routes:
        resp = client.get(route)
        if resp.status_code != 200:
            broken.append(
                f"[INTERNAL] {route} → {resp.status_code} (route exists but failed to render)"
            )
            continue

        html = resp.data.decode("utf-8")
        links = get_links_from_html(html)

        for link in links:
            parsed = urlparse(link)
            if parsed.scheme in ("http", "https"):
                external_links[link] = external_links.get(link, route)
            elif link.startswith("/"):
                path = parsed.path
                if path not in all_internal:
                    broken.append(f"[INTERNAL] {path} → 404  (linked from {route})")
                    all_internal.add(path)  # don't report twice
            # relative links without leading slash — skip for now

    # Check external links
    print(f"Checking {len(external_links)} unique external links...\n")
    session = requests.Session()
    session.headers["User-Agent"] = "Mozilla/5.0 (link checker)"

    for url, source in external_links.items():
        host = urlparse(url).netloc
        try:
            r = session.head(url, timeout=EXTERNAL_TIMEOUT, allow_redirects=True)
            if r.status_code == 405:
                # HEAD not allowed, try GET
                r = session.get(url, timeout=EXTERNAL_TIMEOUT, allow_redirects=True)
            if r.status_code >= 400:
                if r.status_code in (403, 406) or any(fh in host for fh in FLAKY_HOSTS):
                    warnings.append(
                        f"[WARN]   {url} → {r.status_code}  (may block bots, linked from {source})"
                    )
                else:
                    broken.append(
                        f"[BROKEN] {url} → {r.status_code}  (linked from {source})"
                    )
            else:
                print(f"  ✓ {url}")
        except requests.exceptions.RequestException as e:
            broken.append(
                f"[ERROR]  {url} → {type(e).__name__}  (linked from {source})"
            )

    print()
    if warnings:
        print("=== Warnings (may be false positives) ===")
        for w in warnings:
            print(f"  {w}")
        print()

    if broken:
        print("=== Broken links ===")
        for b in broken:
            print(f"  {b}")
        print()
        print(f"{len(broken)} broken link(s) found.")
        return 1
    else:
        print("All links OK.")
        return 0


if __name__ == "__main__":
    sys.exit(check_links())
