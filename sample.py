import tweepy
import json
f = open('keys.json')
keys = json.load(f)
# consumer_key = None
consumer_key = keys['api_key']
consumer_secret = keys['api_secret']
access_token = keys['token']
access_token_secret = keys['token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
timeline = api.user_timeline(id='realDonaldTrump',count=20)
print timeline
