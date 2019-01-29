from flask import Blueprint
from flask import render_template

# This is the blueprint object that gets registered into the app in blueprints.py.
index = Blueprint('index', __name__)


@index.route("/")
def index_page():
    return "Hello"
