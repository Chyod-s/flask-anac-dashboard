""" Módulo com o carregador de usuários. """
from flask_login import LoginManager
from app.extensions import db
from app.repositories import Usuarios

def user_loader(app):
    """ Configura o carregador de usuários. """
    lm = LoginManager(app)
    @lm.user_loader
    def load_user(user_id):
        usuario = db.session.query(Usuarios).filter_by(id=user_id).first()
        return usuario
