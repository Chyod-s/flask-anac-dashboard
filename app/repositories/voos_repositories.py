""" Modelo de dados para a tabela voos """
from app.extensions.flask_extensions import db

class Voos(db.Model):
    """ Modelo de dados para a tabela voos """
    __tablename__ = 'voos'
    id = db.Column(db.Integer, primary_key=True)
    ano = db.Column(db.Integer)
    mes = db.Column(db.Integer)
    mercado = db.Column(db.String(50))
    rpk = db.Column(db.Float)

    def to_dict(self):
        """Converte a instância de Voos em um dicionário serializável."""
        return {
            'id': self.id,
            'ano': self.ano,
            'mes': self.mes,
            'mercado': self.mercado,
            'rpk': self.rpk
        }

    def __repr__(self):
        return f'<{self.mercado};{self.rpk};{self.ano};{self.mes}>'
