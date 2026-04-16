import shutil
from pathlib import Path
import yaml
from flask import Flask
from .utils import create_endpoints, create_pages


def _load_data(app):
    data_dir = Path("data")
    if not data_dir.exists():
        return
    for yaml_file in sorted(data_dir.glob("*.yaml")):
        with open(yaml_file, encoding="utf-8") as f:
            app.jinja_env.globals[yaml_file.stem] = yaml.safe_load(f)


def _make_flask_app():
    Path("static/external").mkdir(exist_ok=True)
    # Combine simple.min.css and styles.css into one file for better performance
    with open("node_modules/simpledotcss/simple.min.css") as simple_css:
        simple_content = simple_css.read()
    with open("static/styles/styles.css") as custom_css:
        custom_content = custom_css.read()
    with open("static/external/combined.min.css", "w") as combined:
        combined.write(simple_content + "\n" + custom_content)
    app = Flask(__name__, template_folder="../templates")
    app.static_folder = Path("../static")
    _load_data(app)
    return app


BASE_URL = "https://westsmith.co.uk"


def build_site():
    app = _make_flask_app()
    shutil.rmtree("build", ignore_errors=True)
    shutil.copytree("static", "build/static")
    endpoints = create_endpoints(app, "content")
    create_pages(app, endpoints, build=True)
    with open("build/CNAME", "w") as f:
        f.write("westsmith.co.uk")
    sitemap_urls = "\n".join(
        f"  <url><loc>{BASE_URL}{ep['route_path']}</loc></url>"
        for ep in endpoints.values()
    )
    with open("build/sitemap.xml", "w") as f:
        f.write(
            f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{sitemap_urls}\n"
            f"</urlset>\n"
        )
    with open("build/robots.txt", "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n")


def run_app():
    app = _make_flask_app()
    endpoints = create_endpoints(app, "content")
    create_pages(app, endpoints)
    return app
