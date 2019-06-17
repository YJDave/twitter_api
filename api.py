from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
	# TODO: Add documentation here on how to access API
    def get(self):
        return jsonify({'hello': 'You can query this API in following format'})

api.add_resource(Hello, '/')

if __name__ == '__main__':
    app.run(debug=True)
