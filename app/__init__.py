import shutil
from pathlib import Path
from flask import Flask
from .home import bp as home_bp


def create_app():
    Path("static/external").mkdir(exist_ok=True)
    shutil.copy("node_modules/simpledotcss/simple.min.css", "static/external")
    app = Flask(__name__, template_folder="../templates")
    app.static_folder = Path("../static")
    app.register_blueprint(home_bp, url_prefix="/")
    return app
