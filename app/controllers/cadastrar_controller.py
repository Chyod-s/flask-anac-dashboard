""" Módulo com as rotas da aplicação. """
from flask import request, render_template, redirect
from app.repositories import Usuarios
from app.extensions import db

def cadastrar_controller(app):
    """ Registra as rotas da aplicação. """
    @app.route('/cadastrar', methods=['GET', 'POST'])
    def cadastrar():
        if request.method == 'GET':
            return render_template('cadastrar.html')
        elif request.method == 'POST':
            nome = request.form['nomeForm']
            senha = request.form['senhaForm']

            novo_usuario = Usuarios(nome=nome, senha=senha)
            db.session.add(novo_usuario)
            db.session.commit()

            return redirect('/')
