from bs4 import BeautifulSoup
import os
from pathlib import Path

import markdown
from flask import Flask, render_template, url_for


def _load_markdown(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return markdown.markdown(f.read(), extensions=["fenced_code", "tables"])


def _fix_rel_paths(html_content, base_url):
    soup = BeautifulSoup(html_content, "html.parser")
    for tag in soup.find_all("a", href=True):
        href = tag["href"]
        if href.startswith("./"):
            target = href[2:]
            new_href = f"{base_url}/{target}" if base_url != "/" else f"./{target}"
            tag["href"] = new_href
    return str(soup)


def _file_to_paths(root, file, md_dir):
    full_path = os.path.join(root, file)
    rel_path = os.path.relpath(full_path, md_dir)
    route_parts = rel_path.replace("\\", "/").split("/")

    is_index = file == "index.md"
    if is_index:
        route_parts = route_parts[:-1]
    else:
        route_parts[-1] = file[:-3]  # remove '.md'

    route_path = "/" + "/".join(route_parts)
    return full_path, route_parts, route_path


def _dir_to_paths(root, dir, md_dir):
    full_path = os.path.join(root, dir)
    rel_path = os.path.relpath(full_path, md_dir)
    route_parts = rel_path.replace("\\", "/").split("/")
    route_parts[-1] = dir
    route_path = "/" + "/".join(route_parts)
    return route_parts, route_path


def build_title(route_parts):
    title_parts = []
    if not route_parts:
        return "Productivity tools and custom software development"  # TODO - make home title configurable
    else:
        for part in route_parts:
            title_parts.append(part.replace("-", " ").capitalize())
    return " - ".join(title_parts)


def create_endpoints(app: Flask, md_dir: str):
    """
    Create a bunch of routes in the flask app from the markdown files. It also outputs
    other data and meta-data from the markdown files such as the page title, link or
    url to the endpoint (derived from the location of the markdown file) and the
    html content rendered from the markdown content.
    """
    endpoints = {}
    for root, dirs, files in os.walk(md_dir):
        for file in files:
            full_path, route_parts, route_path = _file_to_paths(root, file, md_dir)
            # nav = build_nav(dirs, files, root, md_dir) if file == "index.md" else {}
            title = build_title(route_parts)

            endpoint_name = ".".join(route_parts) or "index"
            html_content = _load_markdown(full_path)
            html_content = _fix_rel_paths(html_content, route_path)

            print(f"Adding {endpoint_name} ({route_path})")
            app.add_url_rule(
                route_path,
                endpoint=endpoint_name,
            )
            with app.app_context(), app.test_request_context():
                endpoints[endpoint_name] = {
                    "title": title,
                    "link": url_for(endpoint_name),
                    "route_path": route_path,
                    "html_content": html_content,
                }
    return endpoints


def create_pages(app, endpoints, build=False):
    """Adds the view function that renders that page for Flask and for building,
    will output the html file."""
    for endpoint_name, endpoint in endpoints.items():

        template_path = endpoint["route_path"].lstrip("/")
        if not template_path:
            template_path = "index"
        template_name = f"{template_path}.html"
        template_file = f"templates/{template_name}"
        template_to_use = (
            template_name if os.path.exists(template_file) else "page.html"
        )

        def make_view(content, title, template):
            def view():
                return render_template(
                    template,
                    content=content,
                    title=title,
                    nav=endpoints,
                )

            return view

        app.view_functions[endpoint_name] = make_view(
            endpoint["html_content"], endpoint["title"], template_to_use
        )
        if build:
            Path(f"build{endpoint["route_path"]}").mkdir(parents=True, exist_ok=True)
            with open(f"build{endpoint["route_path"]}/index.html", "w") as f:
                with app.app_context(), app.test_request_context():
                    f.write(make_view(endpoint["html_content"], endpoint["title"])())
