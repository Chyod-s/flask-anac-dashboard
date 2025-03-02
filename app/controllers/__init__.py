""" Módulo de rotas da aplicação. """
from .home_controller import home_controller
from .cadastrar_controller import cadastrar_controller

def register_routes(app):
    """ Registra as rotas da aplicação. """
    home_controller(app)
    cadastrar_controller(app)
