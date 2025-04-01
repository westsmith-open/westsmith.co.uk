from flask import Blueprint, render_template

bp = Blueprint(__name__.split(".")[0], __name__)


@bp.route("/")
def home():
    return render_template("index.html")
