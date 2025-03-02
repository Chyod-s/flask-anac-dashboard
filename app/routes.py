from flask import jsonify, request, render_template, redirect
from .models import Usuarios
from .extensions import db

def register_routes(app):

    @app.route('/', methods=['GET'])
    def home():
        return render_template('home.html')

    @app.route('/cadastrar', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('cadastrar.html')
        elif request.method == 'POST':
            nome = request.form['nomeForm']
            senha = request.form['senhaForm']

            novo_usuario = Usuarios(nome=nome, senha=senha)
            db.session.add(novo_usuario)
            db.session.commit()

            return redirect('/')