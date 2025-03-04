""" Módulo de rotas da aplicação. """
from .info_controller import info_controller
from .get_data_bd import get_data_bd
from .analise_controller import analise_controller
from .logout_controller import logout_controller
from .login_controller import login_controller
from .user_loader import user_loader
from .home_controller import home_controller
from .cadastrar_controller import cadastrar_controller

def register_routes(app):
    """ Registra as rotas da aplicação. """
    home_controller(app)
    cadastrar_controller(app)
    user_loader(app)
    login_controller(app)
    logout_controller(app)
    analise_controller(app)
    get_data_bd(app)
    info_controller(app)
