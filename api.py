from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import os

import db_scripts
from tweepy_func import get_tweets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)

class Hello(Resource):
    # TODO: Add documentation here on how to access API
    def get(self):
        return jsonify({'hello': 'You can query this API in following format'})

class QueryAPI(Resource):
    # TODO: Return tweets here match with keyword
    def get(self, keyword):
        tweets = db_scripts.get_keyword_tweets(keyword)
        if len(tweets) == 0:
            tweets = get_tweets(keyword)
            db_scripts.store_tweets_to_db(keyword, tweets)
        return jsonify(tweets)

api.add_resource(Hello, '/')
api.add_resource(QueryAPI, '/query/<string:keyword>')


if __name__ == '__main__':
    app.run(debug=True)
