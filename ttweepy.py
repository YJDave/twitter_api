# This is extended version of tweepy library to return data from Twitter API
# https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html
# Tweet URL: https://twitter.com/<author_username>/status/<tweet_id>

from tweepy import (
    OAuthHandler,
    API,
    Cursor,
)

from debug import print_msg

MAXIMUM_SEARCH_RESULT = 2

def get_tokens():
    tokens =  {
        "consumer_key": '',
        "consumer_secret": '',
    }
    return tokens["consumer_key"], tokens["consumer_secret"]

def parse_tweet_info(status):
    tweet = {}

    # Tweet metadata
    tweet['text'] = status.text
    tweet['id_str'] = status.id_str
    tweet['created_at'] = status.created_at

    # Tweet likes, retweets..
    tweet['retweet_count'] = status.retweet_count
    tweet['favorite_count'] = status.favorite_count
    tweet['reply_count'] = status.reply_count
    tweet['quote_count'] = status.quote_count

    # Tweet author information
    tweet['author'] = {}
    tweet['author']['name'] = status._json['user']['name']
    tweet['author']['username'] = status._json['user']['screen_name']
    tweet['author']['id_str'] = status._json['user']['id_str']

    return tweet

def authenticate_user():
    consumer_key, consumer_secret = get_tokens()
    auth = OAuthHandler(consumer_key, consumer_secret)

    global api
    api = API(auth)

def search_tweets_by_keywords(keyword):
    ResultObjects = []
    try:
        for StatusObject in Cursor(api.search, q=keyword).items(MAXIMUM_SEARCH_RESULT):
            ResultObjects.append(parse_tweet_info(StatusObject))

    except Exception as e:
        print_msg(e)
    return ResultObjects

def get_tweets(keyword):
    # TODO: Fetch tweets of keywords from Twitter API
    print_msg("Authenticating user...")
    authenticate_user()
    print_msg("Done!")

    print_msg("Fetching tweets of keyword %s..." % (keyword))
    search_result_general = search_tweets_by_keywords(keyword)
    print_msg("Done!")

    return search_result_general
