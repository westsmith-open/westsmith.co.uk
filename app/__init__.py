import shutil
from pathlib import Path
from flask import Flask
from .home import bp as home_bp
from .products import bp as products_bp
from .services import bp as services_bp
from .about import bp as about_bp


def create_app():
    Path("static/external").mkdir(exist_ok=True)
    shutil.copy("node_modules/simpledotcss/simple.min.css", "static/external")
    app = Flask(__name__, template_folder="../templates")
    app.static_folder = Path("../static")
    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(services_bp, url_prefix="/services")
    app.register_blueprint(about_bp, url_prefix="/about")
    return app
