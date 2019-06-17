# This is extended version of tweepy library to return data from Twitter API

from tweepy import (
    OAuthHandler,
    API,
)

def get_tokens():
    tokens =  {
        "consumer_key": '',
        "consumer_secret": '',
        "access_token": '',
        "access_secret": '',
    }
    return tokens.consumer_key, tokens.consumer_secret,
        tokens.access_token, tokens.access_secret

def authenticate_user():
    consumer_key, consumer_secret, access_token, access_secret = get_tokens()

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    #tweeter.api take arguments like auth_handler, host, search_host,..
    global api
    api = API(auth)


def get_tweets(keyword):
    # TODO: Fetch tweets of keywords from Twitter API
    print("Fetching tweets of keyword %s" % (keyword))
    return {}
