""" Logout Controller """
from flask import redirect, url_for
from flask_login import login_required, logout_user

def logout_controller(app):
    """ Registra as rotas da aplicação. """
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('home'))
