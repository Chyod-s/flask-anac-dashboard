""" Login controller """
from flask import render_template, request
from flask_login import login_user
from app.repositories import Usuarios
from app.extensions import db

def login_controller(app):
    """ Registra as rotas da aplicação. """
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            nome = request.form['nome']
            senha = request.form['senha']

            if nome == "" or senha == "":
                return render_template('login.html', erro="Usuário ou senha incorretos")

            user = db.session.query(Usuarios).filter_by(nome=nome).first()
            if user and user.verificar_senha(senha):
                login_user(user)
                return """
                <script>
                    window.parent.location.reload(); 
                </script>
                """
            else:
                return render_template('login.html', erro="Usuário ou senha incorretos")
