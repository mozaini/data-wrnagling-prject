import requests
import os
import pandas as pd
import tweepy
import json



df = pd.read_csv('dataset'+ '/'+'twitter-archive-enhanced.csv', parse_dates=True)


ACCESS_TOKEN = ""  
ACCESS_TOKEN_SECRET = ""  
CONSUMER_KEY = "" 
CONSUMER_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

data = {}
data['tweet_info']=  []
print('{:20s}{:15}{}'.format("Tweet id", "retweet count",'Likes count'))
for i in df['tweet_id']:
    try:
        tweet = api.get_status(i)
        print('{:}{:10d}{:15}'.format(i, tweet.retweet_count,tweet.favorite_count))
        data['tweet_info'].append({
            "tweet_id" : i ,
            "retweet_count": tweet.retweet_count ,
            "likes_count" : tweet.favorite_count
        })
    except:
        print("Id was not found")

with open('tweet_json.txt', 'w') as outfile:
    json.dump(data, outfile)