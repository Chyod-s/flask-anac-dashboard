""" Script para inserir voos no banco de dados a partir de um arquivo CSV. """
import csv
import os
from flask import current_app
from app.repositories import Voos
from app.extensions import db


class InserirVoosCsv():
    """ Insere voos no banco de dados a partir de um arquivo CSV. """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    csv_path = os.path.normpath(os.path.join(
        BASE_DIR, "..", "..", "data", "Dados_Estatisticos.csv"))

    @staticmethod
    def inserir():
        """ Lê o CSV e insere os dados no banco de dados. """
        with current_app.app_context():
            if Voos.query.first():
                return

            with open(InserirVoosCsv.csv_path, 'r', encoding='utf-8') as file:
                next(file)
                reader = csv.DictReader(file, delimiter=";")

                for row in reader:
                    mercado = row["AEROPORTO_DE_ORIGEM_SIGLA"] + row["AEROPORTO_DE_DESTINO_SIGLA"]

                    if row["RPK"] == '':
                        row["RPK"] = 0

                    novo_voo = Voos(
                        ano=row["ANO"],
                        mes=row["MÊS"],
                        mercado=mercado,
                        rpk=row["RPK"]
                    )
                    db.session.add(novo_voo)

                db.session.commit()
