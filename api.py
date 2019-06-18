from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import os

import db_scripts
from tweepy_func import get_tweets

app = Flask(__name__)
app.config.from_object("config.Config")
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

class QueryDBAPITweet(Resource):
    def get(self, option):
        if option not in ['retweet', 'like']:
            return jsonify({"ERROR": "Invalid option"})

        tweets = db_scripts.get_top_tweets(option)
        return jsonify(tweets)

class QueryDBAPIUser(Resource):
    def get(self, keyword):
        all_users = db_scripts.get_users_by_keyword(keyword)
        return jsonify(all_users)

class QueryDBAPIKeyword(Resource):
    def get(self):

        all_tweets = db_scripts.get_all_tweets_keywords()
        return jsonify(all_tweets)

api.add_resource(Hello, '/')
api.add_resource(QueryAPI, '/query/<string:keyword>')
api.add_resource(QueryDBAPITweet, '/query/db/top/<string:option>')
api.add_resource(QueryDBAPIUser, '/query/db/user_tweet/<string:keyword>')
api.add_resource(QueryDBAPIKeyword, '/query/db/all')


if __name__ == '__main__':
    app.run(debug=True)
