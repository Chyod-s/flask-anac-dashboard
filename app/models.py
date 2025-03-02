from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Voos(db.Model):
    __tablename__ = 'voos'
    id = db.Column(db.Integer, primary_key=True)
    ano = db.Column(db.Integer)
    mes = db.Column(db.Integer)
    mercado = db.Column(db.String(50))
    rpk = db.Column(db.Float)

    def __repr__(self):
        return f'<Voo {self.mercado} - {self.ano}/{self.mes}>'

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), unique=True)
    senha = db.Column(db.String(256), nullable=False)

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return f'<Login {self.nome}>'