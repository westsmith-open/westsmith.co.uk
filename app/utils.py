import os
import markdown
from flask import Flask, render_template


def load_markdown(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return markdown.markdown(f.read(), extensions=["fenced_code", "tables"])


def create_routes(app: Flask, md_dir: str):
    for root, dirs, files in os.walk(md_dir):
        for file in files:
            if not file.endswith(".md"):
                continue

            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, md_dir)
            route_parts = rel_path.replace("\\", "/").split("/")

            is_index = file == "index.md"
            if is_index:
                route_parts = route_parts[:-1]
            else:
                route_parts[-1] = file[:-3]  # remove '.md'

            route_path = "/" + "/".join(route_parts)
            if is_index:
                route_path += "/"  # Ensure trailing slash for index pages

            endpoint_name = ".".join(route_parts) or "index"
            html_content = load_markdown(full_path)

            def make_view(content, title=route_parts[-1] if route_parts else "Home"):
                def view():
                    return render_template(
                        "page.html", content=content, title=title.capitalize()
                    )

                return view

            app.add_url_rule(
                route_path, endpoint=endpoint_name, view_func=make_view(html_content)
            )
            print(f"Adding {endpoint_name} ({route_path})")
