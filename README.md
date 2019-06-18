##How to Run?

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
```
python3
>> from models import *
>> db.create_all()
```

7. Add environement variables
`export COUNSUMER_KEY=''`
`export COUNSUMER_SECRET=''`
`export DATABASE_URL=''`

8. Run application
`python api.py`

9. Run celery
`celery -A api.celery worker --loglevel=info`
`celery beat -A api.celery --loglevel=INFO`

10. Run rabbimq
`brew services start rabbitmq`

11. Query API
Following are avaliable API endpoints

`/query/<string:keyword>`
Returns tweets searched by keywords
If database already have stored results, then fetch from database
Otherwise fetch from Twitter API and store the results

`/query/db/top/<string:option>`
Option can be either "retweet" or "like"
Returns tweets stored in database in descending order or likes or retweets

`/query/db/user_tweet/<string:keyword>`
Returns all authors ids, who tweet on given keyword, with count of tweets

`/query/db/all`
Returns all stored tweets group by keywords


##Examples

1. `curl http://127.0.0.1:5000/query/modi`
Output:
```
[
  {
    "author_id_str": "164738585",
    "created_at": "Tue, 18 Jun 2019 07:50:01 GMT",
    "favorite_count": 0,
    "id_str": "1140889388655599616",
    "retweet_count": 396,
    "text": "RT @BoltaHindustan: \u0932\u094b\u0915\u0938\u092d\u093e \u091a\u0941\u0928\u093e\u0935 \u0915\u0947 \u0938\u092e\u092f 13 \u092c\u093e\u0930 '\u092c\u093f\u0939\u093e\u0930 \u0926\u094c\u0930\u093e' \u0915\u0930\u0928\u0947 \u0935\u093e\u0932\u0947 \u0938\u093e\u0939\u0947\u092c 100 \u092c\u091a\u094d\u091a\u094b\u0902 \u0915\u0940 \u092e\u094c\u0924 \u092a\u0930 \u0916\u093e\u092e\u094b\u0936 \u0915\u094d\u092f\u094b\u0902 \u0939\u0948? : @ratanlal72 \n\n#Bihar #Lo\u2026"
  },
  {
    "author_id_str": "95404086",
    "created_at": "Tue, 18 Jun 2019 07:50:01 GMT",
    "favorite_count": 0,
    "id_str": "1140889386122223617",
    "retweet_count": 0,
    "text": "BJP's friend Ramdev calls Modi govt arrogant, lauds Rahul for being on right track https://t.co/3QpzhMo5AS via @indiatoday"
  },
  {
    "author_id_str": "1068471795538259969",
    "created_at": "Tue, 18 Jun 2019 07:50:00 GMT",
    "favorite_count": 0,
    "id_str": "1140889382771015680",
    "retweet_count": 0,
    "text": "\u0906\u0902\u0924\u0930\u0930\u093e\u0937\u094d\u091f\u094d\u0930\u0940\u092f \u0938\u094d\u0924\u0930\u093e\u0935\u0930\u0940\u0932 \u0924\u0923\u093e\u0935\u093e\u091a\u094d\u092f\u093e \u092a\u0930\u093f\u0938\u094d\u0925\u093f\u0924\u0940\u0924 \u092d\u093e\u0930\u0924\u093e\u0932\u093e \u0906\u092a\u0932\u0947 \u092d\u0942\u0930\u093e\u091c\u0915\u0940\u092f \u0906\u0923\u093f \u092d\u0942\u0938\u093e\u092e\u0930\u093f\u0915 \u0938\u094d\u0925\u093e\u0928 \u0938\u092e\u0930\u094d\u0925\u092a\u0923\u0947 \u0924\u094b\u0932\u0942\u0928 \u0927\u0930\u093e\u0935\u0947 \u0932\u093e\u0917\u0923\u093e\u0930 \u0906\u2026 https://t.co/qdZCXfBo4p"
  }
]
```

2. `curl http://127.0.0.1:5000/query/db/top/like`

```
[
  {
    "author_id_str": "1139776066376126464",
    "favorite_count": 1,
    "id_str": "1139780908213424129",
    "retweet_count": 0,
    "text": "@narendramodi my name is yashashvi srivastava. i lives in mumbai with my parents. i am graduate and secure highest\u2026 https://t.co/Kv3AYIeQVI"
  },
  {
    "author_id_str": "2223150613",
    "favorite_count": 0,
    "id_str": "1140890295216685056",
    "retweet_count": 0,
    "text": "PM Modi working on new, updated edition of his book \u2018Exam Warriors\u2019\nhttps://t.co/CjXJwvc4As via NaMo App https://t.co/brhco0Kxes"
  },
  {
    "author_id_str": "924888602936451072",
    "favorite_count": 0,
    "id_str": "1140890312576946176",
    "retweet_count": 0,
    "text": "@narendramodi modi g im Mallesh no network Jio Yammehatti dk halli p shivamoga d Bhadravathi t pn cood 577227 no re\u2026 https://t.co/Yfnrz3yeb2"
  },
]
```

3. `curl http://127.0.0.1:5000/query/db/user_tweet/modi`

```
{
  "2223150613": {
    "User ID": "2223150613",
    "count": 1
  },
  "4069549338": {
    "User ID": "4069549338",
    "count": 1
  },
  "924888602936451072": {
    "User ID": "924888602936451072",
    "count": 1
  }
}
```

4. `curl http://127.0.0.1:5000/query/db/all`

```
{
  "cricket": [
    {
      "author_id_str": "148798507",
      "favorite_count": 0,
      "id_str": "1140890338086871040",
      "retweet_count": 0,
      "text": "@realshoaibmalik Tum jesa neech insan shayed pakistan ki tarekh mein na ho jis tarhan tum nay pak cricket ko barbad\u2026 https://t.co/z0CMhPRF6p"
    },
    {
      "author_id_str": "2564755236",
      "favorite_count": 0,
      "id_str": "1140890337746944000",
      "retweet_count": 1487,
      "text": "RT @RanveerOfficial: I've been a die-hard fan of Indian cricket since childhood. Invested so much emotion into our beloved team. Willing an\u2026"
    },
    {
      "author_id_str": "1047548457316208640",
      "favorite_count": 0,
      "id_str": "1140890329295523840",
      "retweet_count": 3,
      "text": "RT @SherazAS1: With a very angry heart I hv to share some facts. This is the same @TheRealPCB  destroyed so many talented plyrs frm Pak cri\u2026"
    }
  ],
  "django": [
    {
      "author_id_str": "838866096535003136",
      "favorite_count": 0,
      "id_str": "1140889837010149377",
      "retweet_count": 4,
      "text": "RT @art_bosch: @WhiteHouse \ud83c\udf3b\ud83c\udf3b\ud83c\udf3b Should Americans prepare for another Stupid War brought to us by REPUBLICANS and DoTard Trump! https://t.co/\u2026"
    },
    {
      "author_id_str": "838866096535003136",
      "favorite_count": 0,
      "id_str": "1140889673574899712",
      "retweet_count": 1374,
      "text": "RT @ProudResister: The latest reporting from the Washington Post is disturbing:\n\nPelosi is waging a behind the scenes campaign *AGAINST* im\u2026"
    },
    {
      "author_id_str": "1634715152",
      "favorite_count": 0,
      "id_str": "1140889624413462529",
      "retweet_count": 0,
      "text": "@RealChrisSean Ever mess with django?"
    }
  ],
}
```

##Resources

* https://www.youtube.com/watch?v=s_ht4AKnWZg
* https://github.com/pallets/flask/blob/master/.gitignore
* https://flask-restful.readthedocs.io/en/latest/quickstart.html
* https://developer.twitter.com/en/docs/tweets/search/overview/standard
* http://docs.tweepy.org/en/v3.5.0/
* https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html
* https://stackoverflow.com/questions/7975556/how-to-start-postgresql-server-on-mac-os-x
* https://www.codementor.io/olawalealadeusi896/restful-api-with-python-flask-framework-and-postgres-db-part-1-kbrwbygx5
* https://www.youtube.com/watch?v=OvhoYbjtiKc
* https://stackoverflow.com/questions/25668092/flask-sqlalchemy-many-to-many-insert-data

