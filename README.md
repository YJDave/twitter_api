1. You have to fetch data from Twitter API, you have to extend an API using which user can query Twitter and fetch all tweets.
(In simple words you have to create a wrapper on top of Twitter API)
    1.1 You have to fetch all the tweets and store in mongo/PostgreSQL once a user searches for them via your API
    1.2 You have to auto refresh latest tweets every 10 minutes, you can use celery beats for doing this.

2. Once stored all data in mongo/PostgreSQL, you have to expose multiple or a single endpoint for returning stats of the tweets
that were pulled.
     2.1 API to fetch all the users who had a tweet on the requested text, with a count of tweets
     2.2 API to fetch top tweets based on likes, retweets
     2.3 Total Numbers of tweets stored in DB group by keywords


**How to Run?
1. Create virtual env
`virtualenv <env_name> -p python3`

2. Login to venv
`source <env_name>/bin/activate`

3. Install requirements
`pip install -r requirements.txt`

4. Start psql
`pg_ctl -D /usr/local/var/postgres start`

5. Create Database
`createdb <db_name>`

6. Create tables
`
>> from models import *
>> db.create_all()
`

7. Add environement variables
`export COUNSUMER_KEY=''`
`export COUNSUMER_SECRET=''`
`export DATABASE_URL=''`

8. Run application
`python api.py`

9. Query API
Following are avaliable API endpoints
`/query/<string:keyword>`
> Returns tweets searched by keywords
> If database already have stored results, then fetch from database
> Otherwise fetch from Twitter API and store the results

`/query/db/top/<string:option>`
> Option can be either "retweet" or "like"
> Returns tweets stored in database in descending order or likes or retweets

`/query/db/user_tweet/<string:keyword>`
> Returns all authors ids, who tweet on given keyword, with count of tweets

`/query/db/all`
> Returns all stored tweets group by keywords
