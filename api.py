from flask import Flask, jsonify
from flask_restful import Resource, Api

from db_scripts import store_tweets_to_db
from ttweepy import get_tweets

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    # TODO: Add documentation here on how to access API
    def get(self):
        return jsonify({'hello': 'You can query this API in following format'})

class QueryAPI(Resource):
    # TODO: Return tweets here match with keyword
    def get(self, keyword):
        store_tweets_to_db()
        tweets = get_tweets(keyword)
        return jsonify(tweets)

api.add_resource(Hello, '/')
api.add_resource(QueryAPI, '/query/<string:keyword>')


if __name__ == '__main__':
    app.run(debug=True)
