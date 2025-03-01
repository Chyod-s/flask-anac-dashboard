import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///anac_flight_database.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
