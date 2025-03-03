""" Módulo com as rotas da aplicação. """
from flask import render_template
from flask_login import login_required

def analise_controller(app):
    """ Registra as rotas da aplicação. """
    @app.route('/analise', methods=['GET'])
    @login_required
    def analise():
        return render_template('analise.html')
