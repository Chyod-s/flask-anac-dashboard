""" Módulo de configurações da aplicação """
import os

class Config:
    """ Configurações da aplicação """
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///anac_flight_database.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
