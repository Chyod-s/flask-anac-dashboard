from flask import jsonify, request, render_template

def register_routes(app):

    @app.route('/', methods=['GET'])
    def initial_route():
        return jsonify({'message': 'Hello World!'})

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
           