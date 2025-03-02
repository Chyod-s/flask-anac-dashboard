""" Módulo de rotas da aplicação. """
from .user_loader import user_loader
from .home_controller import home_controller
from .cadastrar_controller import cadastrar_controller

def register_routes(app):
    """ Registra as rotas da aplicação. """
    home_controller(app)
    cadastrar_controller(app)
    user_loader(app)
