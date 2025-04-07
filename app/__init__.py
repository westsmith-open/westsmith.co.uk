import shutil
from pathlib import Path
from flask import Flask
from .utils import create_routes


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
    create_routes(app, "content", build=True)


def run_app():
    app = _make_flask_app()
    create_routes(app, "content")
    return app
