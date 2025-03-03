""" Módulo com as rotas da aplicação. """
from flask import render_template
from flask_login import login_required

def home_controller(app):
    """ Registra as rotas da aplicação. """
    @app.route('/', methods=['GET'])
    @login_required
    def home():
        return render_template('home.html')
