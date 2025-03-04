""" Módulo de inicialização da aplicação Flask """
import os
from flask import Flask
from app.comandos import register_commands
from app.controllers import register_routes
from app.extensions import Config, db, migrate

KEY = os.getenv('SECRET_KEY')
if not KEY:
    KEY = 'T&st3-T0k3n'

def create_app():
    """ Cria a aplicação Flask """
    app = Flask(__name__)
    app.secret_key = KEY

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.repositories import Usuarios, Voos # pylint: disable=C0415,W0611

    register_routes(app)

    register_commands(app)

    return app
