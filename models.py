
import datetime
from api import db

search_results = db.Table('results',
    db.Column('keyword', db.String(120), db.ForeignKey('keyword.name')),
    db.Column('tweet', db.Integer, db.ForeignKey('tweet.t_id')),
)

class TweetModel(db.Model):
    __tablename__ = 'tweet'

    t_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    retweet_count = db.Column(db.Integer, nullable=False)
    favorite_count = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, nullable=False)

    keywords = db.relationship('SearchKeyword', secondary=search_results,
                                backref=db.backref('tweets'), lazy='dynamic')

class SearchKeyword(db.Model):
    __tablename__ = "keyword"
    name = db.Column(db.String(120), primary_key=True)
    last_updated = db.Column(db.DateTime, nullable=False)
