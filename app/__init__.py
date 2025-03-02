""" Módulo de inicialização da aplicação Flask """
from flask import Flask
from app.comandos import register_commands
from app.controllers import register_routes
from app.extensions import Config, db, migrate

def create_app():
    """ Cria a aplicação Flask """
    app = Flask(__name__)
    app.secret_key = '(v!z.MhM?Ci`!pHL?.'

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.repositories import Usuarios, Voos # pylint: disable=C0415,W0611

    register_routes(app)

    register_commands(app)

    return app
