""" Arquivo de inicialização da aplicação Flask """
from os import environ
from app import create_app

def main():
    """ Inicializa a aplicação Flask """
    app = create_app()

    server_host = environ.get('SERVER_HOST', 'localhost')
    app.run(host=server_host, port=5500, debug=True)

if __name__ == '__main__':
    main()
