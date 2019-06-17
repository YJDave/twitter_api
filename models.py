
import datetime
from api import db
from sqlalchemy import func
from sqlalchemy.sql import label

search_results = db.Table('results',
    db.Column('keyword', db.String(120), db.ForeignKey('keyword.name')),
    db.Column('tweet', db.String(20), db.ForeignKey('tweet.t_id')),
)

class TweetModel(db.Model):
    __tablename__ = 'tweet'

    t_id = db.Column(db.String(20), primary_key=True)
    text = db.Column(db.String(280), nullable=False)
    # created_at = db.Column(db.DateTime, nullable=False)
    retweet_count = db.Column(db.Integer, nullable=False)
    # TODO: Fix the spell mistake here
    favorite_count = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.String(20), nullable=False)

    keywords = db.relationship('SearchKeyword', secondary=search_results,
                                backref=db.backref('tweets'), lazy='dynamic')


    def __init__(self, data):
        self.t_id = int(data.get('id_str'))
        self.text = data.get('text')
        # TODO: Parse this to datetime here, cause it is string
        # self.created_at = data.get('created_at')
        self.retweet_count = data.get('retweet_count')
        self.favorite_count = data.get('favorite_count')
        self.author_id = int(data.get('author_id_str'))

    def update(self, keyword):
        self.keywords.append(keyword)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        tweet = {}
        tweet['text'] = self.text
        tweet['id_str'] = self.t_id
        tweet['retweet_count'] = self.retweet_count
        tweet['favorite_count'] = self.favorite_count
        tweet['author_id_str'] = self.author_id
        return tweet

    @staticmethod
    def get_authors_group_by(keyword):
        # TODO: Add efficient query and remove function in db_script
        return []

    @staticmethod
    def get_tweet(t_id):
        return TweetModel.query.get(t_id)

class SearchKeyword(db.Model):
    __tablename__ = "keyword"
    name = db.Column(db.String(120), primary_key=True)
    last_updated = db.Column(db.DateTime, nullable=False)

    def __init__(self, keyword):
        self.name = keyword
        self.last_updated = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.last_updated = datetime.datetime.utcnow()
        db.session.commit()

    @staticmethod
    def get_keyword(keyword):
        return SearchKeyword.query.get(keyword)
