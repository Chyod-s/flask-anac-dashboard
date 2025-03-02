from app import db

class Voos(db.Model):
    __tablename__ = 'voos'
    id = db.Column(db.Integer, primary_key=True)
    ano = db.Column(db.Integer)
    mes = db.Column(db.Integer)
    mercado = db.Column(db.String(50))
    rpk = db.Column(db.Float)

    def __repr__(self):
        return f'<Voo {self.mercado} - {self.ano}/{self.mes}>'

class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    senha = db.Column(db.Integer)

    def __repr__(self):
        return f'<Login {self.nome}>'