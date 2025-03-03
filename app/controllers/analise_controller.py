""" Módulo com as rotas da aplicação. """
from flask import render_template

def analise_controller(app):
    """ Registra as rotas da aplicação. """
    @app.route('/analise', methods=['GET'])
    def analise():
        return render_template('analise.html')
