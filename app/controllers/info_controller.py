""" Módulo com as rotas da aplicação. """
from flask import render_template

def info_controller(app):
    """ Registra as rotas da aplicação. """
    @app.route('/info', methods=['GET'])
    def info():
        return render_template('info.html')
