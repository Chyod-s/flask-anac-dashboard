""" Este módulo é responsável por obter dados da base de dados. """
from app.repositories import Voos
from app.extensions import db

class GetData():
    """ Classe responsável por obter dados da base de dados. """
    def __init__(self):
        pass

    def get_data(self):
        """ Obtém dados da base de dados. """
        dados = db.session.query(Voos).all()

        return dados
