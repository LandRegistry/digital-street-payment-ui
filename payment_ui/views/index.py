from flask import Blueprint, redirect, url_for

# This is the blueprint object that gets registered into the app in blueprints.py.
index = Blueprint('index', __name__)


@index.route("/")
def index_page():
    return redirect(url_for('admin.list'))
