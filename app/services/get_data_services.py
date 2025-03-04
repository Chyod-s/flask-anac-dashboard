""" Este módulo é responsável por obter dados da base de dados. """
from app.repositories import Voos
from app.extensions import db

class GetData():
    """ Classe responsável por obter dados da base de dados. """

    @staticmethod
    def get_data():
        """ Obtém dados da base de dados. """
        dados = db.session.query(Voos).all()

        serialized_data = [dado.to_dict() for dado in dados]

        return serialized_data

