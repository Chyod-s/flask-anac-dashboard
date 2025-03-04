""" Módulo de modelos de usuários """
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.extensions import db

class Usuarios(UserMixin, db.Model):
    """ Modelo de dados para a tabela de usuários """
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False, unique=True)
    senha = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, senha, email):
        self.nome = nome
        self.set_senha(senha)
        self.email = email

    def set_senha(self, senha):
        """ Criptografa a senha do usuário """
        self.senha = generate_password_hash(senha)

    def verificar_senha(self, senha):
        """ Verifica se a senha informada é a mesma do usuário """
        return check_password_hash(self.senha, senha)

    def __repr__(self):
        return f'<Login {self.nome} - {self.email}>'
