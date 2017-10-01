from config import config, SELECTED_CONFIG
from flask import Flask
from users.controllers import user

from extensions import db, swagger


def create_app():
    app = Flask(__name__)
    app.config.from_object(config[SELECTED_CONFIG])

    db.init_app(app)
    swagger.init_app(app)

    # Register the blueprints
    app.register_blueprint(user, url_prefix=app.config['APPLICATION_ROOT'])

    return app
