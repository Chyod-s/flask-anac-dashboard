""" Script para inserir voos no banco de dados a partir de um arquivo CSV. """
import csv
import os
import unidecode
from flask import current_app
from app.repositories import Voos
from app.extensions import db

class InserirVoosCsv():
    """ Insere voos no banco de dados a partir de um arquivo CSV. """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    csv_path = os.path.normpath(os.path.join(
        BASE_DIR, "..", "..", "data", "Dados_Estatisticos.csv"))

    @staticmethod
    def filtro_voos(reader):
        """ Filtra os voos de acordo com os parâmetros passados. """
        voos_filtrados = []
        for linha in reader:
            if linha['EMPRESA'] != 'GLO':
                continue

            if linha['GRUPO_DE_VOO'] != 'REGULAR':
                continue

            if linha['NATUREZA'] != 'DOMÉSTICA':
                continue

            voos_filtrados.append(linha)
        return voos_filtrados

    @staticmethod
    def inserir():
        """ Lê o CSV e insere os dados no banco de dados. """
        with current_app.app_context():
            if Voos.query.first():
                return

            with open(InserirVoosCsv.csv_path, 'r', encoding='utf-8') as file:
                next(file)
                reader = csv.DictReader(file, delimiter=";")

                reader.fieldnames = [unidecode.unidecode(col).upper() for col in reader.fieldnames]

                voos_filtrados = InserirVoosCsv.filtro_voos(reader)

                colunas_necessarias = [
                    "ANO", "MES", "AEROPORTO_DE_ORIGEM_SIGLA", "AEROPORTO_DE_DESTINO_SIGLA","RPK"
                    ]

                for row in voos_filtrados:
                    dados_filtrados = {
                        chave: row[chave] for chave in colunas_necessarias if chave in row
                        }

                    mercado = dados_filtrados["AEROPORTO_DE_ORIGEM_SIGLA"] + dados_filtrados["AEROPORTO_DE_DESTINO_SIGLA"] # pylint: disable=C0301

                    if dados_filtrados["RPK"] == '':
                        dados_filtrados["RPK"] = 0

                    novo_voo = Voos(
                        ano=dados_filtrados["ANO"],
                        mes=dados_filtrados["MES"],
                        mercado=mercado,
                        rpk=dados_filtrados["RPK"]
                    )
                    db.session.add(novo_voo)

                db.session.commit()
