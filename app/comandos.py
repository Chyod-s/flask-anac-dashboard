""" Comandos personalizados para o Flask. 
    -flask run-migrations: Roda as migrações do banco de dados.
    -flask inserir-dados-csv: Insere os dados do CSV no banco de dados.
"""
import os
import click
from flask_migrate import upgrade, init, migrate
from flask.cli import with_appcontext
from app.services import InserirVoosCsv

@click.command('run-migrations')
@with_appcontext
def run_migrations():
    """Rodar as migrações do banco de dados."""
    print("Iniciando migração...")

    if not os.path.exists("migrations"):
        init()

    migrate()
    upgrade()

@click.command('inserir-dados-csv')
@with_appcontext
def inserir_dados_csv():
    """Inserir dados do CSV."""
    print("Iniciando inserção de dados...")
    InserirVoosCsv.inserir()
    print("Concluido inserção de dados...")

def register_commands(app):
    """ Registra os comandos personalizados. """
    app.cli.add_command(run_migrations)
    app.cli.add_command(inserir_dados_csv)
