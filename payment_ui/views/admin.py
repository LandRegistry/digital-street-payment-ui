from flask import Blueprint, render_template, url_for, request, redirect, current_app, session
import requests


# This is the blueprint object that gets registered into the app in blueprints.py.
admin = Blueprint('admin', __name__)


@admin.route("/list")
def list():
    # fetch all titles
    try:
        # Fetch all cases of the conveyancer
        titles = requests.get(current_app.config['PAYMENT_API_URL'] + '/titles', headers={'Accept': 'application/json'})

    except requests.exceptions.RequestException as e:
        return render_template('app/admin/list.html', error_message=str(e))

    titles_res = titles.json()

    return render_template('app/admin/list.html', titles=titles_res)


@admin.route("/funds_received", methods=['GET'])
def funds_received():
    title_number = request.args.get('title_number')
    try:
        # api call to confirm funds receipt
        url = current_app.config['PAYMENT_API_URL'] + '/titles/' + title_number + '/confirm-payment'
        response = requests.put(url, headers={'Accept': 'Application/JSON', 'Content-Type': 'Application/JSON'})

        if response.status_code == 200:
            return redirect(url_for('admin.list'))
        else:
            if response.text:
                error_message = response.text
            else:
                error_message = "Error: Payment API failed. Could not return a response."
            return redirect(url_for('admin.list', error_message=error_message))
    except requests.exceptions.RequestException as e:
        return redirect(url_for('admin.list', error_message=str(e)))
