import shutil
from pathlib import Path
from flask import Flask
from .utils import create_endpoints, create_pages


def _make_flask_app():
    Path("static/external").mkdir(exist_ok=True)
    shutil.copy("node_modules/simpledotcss/simple.min.css", "static/external")
    app = Flask(__name__, template_folder="../templates")
    app.static_folder = Path("../static")
    return app


def build_site():
    app = _make_flask_app()
    shutil.rmtree("build", ignore_errors=True)
    shutil.copytree("static", "build/static")
    endpoints = create_endpoints(app, "content")
    create_pages(app, endpoints, build=True)
    with open("build/CNAME", "w") as f:
        f.write("westsmith.co.uk")


def run_app():
    app = _make_flask_app()
    endpoints = create_endpoints(app, "content")
    create_pages(app, endpoints)
    return app
