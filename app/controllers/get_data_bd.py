""" Módulo responsável por registrar as rotas da aplicação. """
from flask import jsonify
from app.services import GetData

def get_data_bd(app):
    """ Registra as rotas da aplicação. """
    @app.route('/get-data', methods=['GET'])
    def get_data():
        """ Obtém dados da base de dados. """
        get_data_service = GetData()
        data = get_data_service.get_data()

        return jsonify(data)
