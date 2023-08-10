from flask import Blueprint

bp = Blueprint("packages", __name__, url_prefix="")

@bp.route("/")
def index():
    return "Package Tracker"