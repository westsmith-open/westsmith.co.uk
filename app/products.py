from flask import Blueprint, render_template

bp = Blueprint("products", __name__)


@bp.route("/")
def index():
    return render_template("products.html")


@bp.route("/word-import-for-monday")
def word_import():
    return render_template("products.html")


@bp.route("/word-import-for-monday/documentation")
def word_import_docs():
    return render_template("products.html")


@bp.route("/word-import-for-monday/pricing")
def word_import_pricing():
    return render_template("products.html")


@bp.route("/word-import-for-monday/terms-of-service")
def word_import_terms():
    return render_template("products.html")


@bp.route("/word-import-for-monday/privacy-policy")
def word_import_privacy():
    return render_template("products.html")


@bp.route("/sprout-for-monday")
def sprout():
    return render_template("products.html")
