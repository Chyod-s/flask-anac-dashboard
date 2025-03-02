""" Módulo com as rotas da aplicação. """
from flask import request, render_template, redirect, url_for
from flask_login import login_user
from app.repositories import Usuarios
from app.extensions import db


def cadastrar_controller(app):
    """ Registra as rotas da aplicação. """
    @app.route('/cadastrar', methods=['GET', 'POST'])
    def cadastrar():
        if request.method == 'GET':
            return render_template('cadastrar.html')
        elif request.method == 'POST':
            nome = request.form['nome']
            senha = request.form['senha']
            email = request.form['email']

            novo_usuario = Usuarios(nome=nome, senha=senha, email=email)
            db.session.add(novo_usuario)
            db.session.commit()

            login_user(novo_usuario)


            return redirect(url_for('home'))
