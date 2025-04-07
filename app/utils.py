from bs4 import BeautifulSoup
import os
from pathlib import Path

import markdown
from flask import Flask, render_template


def _load_markdown(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return markdown.markdown(f.read(), extensions=["fenced_code", "tables"])


def _fix_rel_paths(html_content, base_url):
    soup = BeautifulSoup(html_content, "html.parser")
    for tag in soup.find_all("a", href=True):
        href = tag["href"]
        if href.startswith("./"):
            target = href[2:]
            new_href = f"{base_url}/{target}" if base_url else f"./{target}"
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


def create_routes(app: Flask, md_dir: str, build=False):
    for root, dirs, files in os.walk(md_dir):
        nav = [{"link": "/", "title": "Home"}]
        for file in files:
            _, route_parts, route_path = _file_to_paths(root, file, md_dir)
            if route_path == "/":
                continue
            nav.append({"link": route_path, "title": route_parts[-1].title()})
        for dir in dirs:
            route_parts, route_path = _dir_to_paths(root, dir, md_dir)
            if route_path == "/":
                continue
            nav.append({"link": route_path, "title": route_parts[-1].title()})
        for file in files:
            if not file.endswith(".md"):
                continue

            full_path, route_parts, route_path = _file_to_paths(root, file, md_dir)

            endpoint_name = ".".join(route_parts) or "index"
            html_content = _load_markdown(full_path)
            html_content = _fix_rel_paths(html_content, route_path)

            def make_view(
                content,
                title=(
                    route_parts[-1]
                    if route_parts
                    else "Productivity tools and custom software development"
                ),
            ):
                def view():
                    return render_template(
                        "page.html", content=content, title=title.title(), nav=nav
                    )

                return view

            print(f"Adding {endpoint_name} ({route_path})")
            app.add_url_rule(
                route_path, endpoint=endpoint_name, view_func=make_view(html_content)
            )
            if build:
                Path(f"build{route_path}").mkdir(parents=True, exist_ok=True)
                with open(f"build{route_path}/index.html", "w") as f:
                    with app.app_context(), app.test_request_context():
                        f.write(make_view(html_content)())
