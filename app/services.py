from flask import Blueprint, render_template

bp = Blueprint("services", __name__)


@bp.route("/")
def index():
    return render_template("services.html")
