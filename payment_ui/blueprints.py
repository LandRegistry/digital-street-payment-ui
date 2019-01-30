# Import every blueprint file
from payment_ui.views import general, index, admin


def register_blueprints(app):
    """
    Adds all blueprint objects into the app.
    """
    app.register_blueprint(general.general)
    app.register_blueprint(index.index)
    app.register_blueprint(admin.admin, url_prefix="/admin")

    # All done!
    app.logger.info("Blueprints registered")
