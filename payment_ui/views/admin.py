from flask import Blueprint, render_template, url_for, request, redirect, current_app, session
import requests


# This is the blueprint object that gets registered into the app in blueprints.py.
admin = Blueprint('admin', __name__)


@admin.route("/list")
def list():
    buyer_details = [{
        "buyer": {
            "first_name": "David",
            "last_name": "Jones"
        },
        "conveyancer": {
            "organisation": "conveyancer1"
        },
        "status": "funds_pending"

    }]
    return render_template('app/admin/list.html', buyer_details=buyer_details)
