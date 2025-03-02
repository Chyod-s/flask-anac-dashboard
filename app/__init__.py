from flask import Flask
from config import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import models

    from .routes import register_routes
    register_routes(app)

    return app
