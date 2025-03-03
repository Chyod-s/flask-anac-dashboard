""" Módulo com as rotas da aplicação. """
from flask import render_template

def home_controller(app):
    """ Registra as rotas da aplicação. """
    @app.route('/', methods=['GET'])
    def home():
        return render_template('home.html')
