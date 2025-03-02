from app import create_app
from os import environ

def main():
    app = create_app()

    SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
    app.run(host=SERVER_HOST, port=5500, debug=True)

if __name__ == '__main__':
    main() 