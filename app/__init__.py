from flask import Flask

from app.config.settings import Config

from app.extensions.database import db
from app.extensions.jwt import jwt
from app.extensions.cors import cors

from app.routes.health import health_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    jwt.init_app(app)

    cors.init_app(app)

    app.register_blueprint(
        health_bp
    )

    with app.app_context():
        from app.models import User
        from app.models import Expense

    return app