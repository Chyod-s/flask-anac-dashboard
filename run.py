from flask import Flask
from os import environ
from app.routes import register_routes

def main():
    app = Flask(__name__)

    register_routes(app)

    SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
    app.run(host=SERVER_HOST, port=5500, debug=True)

if __name__ == '__main__':
    main() 