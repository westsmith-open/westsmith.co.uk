from flask import Blueprint, render_template
from .utils import load_markdown

bp = Blueprint("home", __name__)


@bp.route("/")
def index():
    content = load_markdown("index.md")

    return render_template("home.html", content=content)
