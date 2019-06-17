
# Functions to interact with database models
from debug import print_msg
import models

def get_keyword_tweets(keyword):
    print_msg("Checking if keyword exists...")
    tweets = []
    sk = models.SearchKeyword.get_keyword(keyword)
    if sk:
        for tweet in models.TweetModel.query.filter(models.TweetModel.keywords.any(name=keyword)).all():
            tweets.append(tweet.to_dict())
    print_msg("Done!")
    return tweets

def get_top_tweets(option):
    print_msg("Getting top tweets")
    if option == 'retweet':
        query = 'retweet_count'
    elif option == 'like':
        query = 'favorite_count'

    tweets = []
    for tweet in models.TweetModel.query.order_by(query):
        tweets.insert(0, tweet.to_dict())
    print_msg("Done!")
    return tweets

def get_all_tweets_keywords():
    all_tweets = {}
    print_msg("Getting all tweets by keyword...")
    for keyword in models.SearchKeyword.query.all():
        all_tweets[keyword.name] = []
        for tweet in models.TweetModel.query.filter(models.TweetModel.keywords.any(name=keyword.name)).all():
            all_tweets[keyword.name].append(tweet.to_dict())
    print_msg("Done!")
    return all_tweets

def store_tweets_to_db(keyword, tweets):
    # TODO: store tweets to db
    print_msg("Storing tweets to database")
    sk = models.SearchKeyword(keyword)
    for tweet in tweets:
        # print(tweet.get('id_str'))
        s_tweet = models.TweetModel.get_tweet(tweet.get('id_str'))
        if not s_tweet:
            tweetm = models.TweetModel(tweet)
            tweetm.keywords.append(sk)
            tweetm.save()
        else:
            s_tweet.update(sk)
    print_msg("Done!")
