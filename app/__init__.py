from flask import Flask

from app.config.settings import Config

from app.extensions.database import db
from app.extensions.jwt import jwt
from app.extensions.cors import cors
from app.extensions.migrate import migrate
from app.routes.health import health_bp
from app.routes.auth_routes import auth_bp
from app.routes.user_routes import user_bp
from app.routes.expense_routes import (
    expense_bp
)

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    
    migrate.init_app(app, db)

    jwt.init_app(app)

    cors.init_app(app)

    app.register_blueprint(
        health_bp
    )
    
    app.register_blueprint(
        auth_bp
    )
    
    app.register_blueprint(
        user_bp
    )
    
    app.register_blueprint(
        expense_bp
    )

    with app.app_context():
        from app.models import User
        from app.models import Expense

    return app