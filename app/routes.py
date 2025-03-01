from flask import jsonify

def register_routes(app):

    @app.route('/', methods=['GET'])
    def initial_route():
        return jsonify({'message': 'Hello World!'})

    