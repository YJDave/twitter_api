1. You have to fetch data from Twitter API, you have to extend an API using which user can query Twitter and fetch all tweets.
(In simple words you have to create a wrapper on top of Twitter API)
    1.1 You have to fetch all the tweets and store in mongo/PostgreSQL once a user searches for them via your API
    1.2 You have to auto refresh latest tweets every 10 minutes, you can use celery beats for doing this.

2. Once stored all data in mongo/PostgreSQL, you have to expose multiple or a single endpoint for returning stats of the tweets
that were pulled.
     2.1 API to fetch all the users who had a tweet on the requested text, with a count of tweets
     2.2 API to fetch top tweets based on likes, retweets
     2.3 Total Numbers of tweets stored in DB group by keywords


