# Imports

import tweepy
import json

# CONATANTS

# SETTING UP ACCESS TO TWITTER
TWEET_ADMIN = open('tweet_api.json')
ADMIN_DATA = json.load(TWEET_ADMIN)
API_KEY = ADMIN_DATA.get('api_key')
API_KEY_SECRET = ADMIN_DATA.get('api_key_secret')
ACCESS_TOKEN = ADMIN_DATA.get('access_token')
ACCESS_TOKEN_SECRET = ADMIN_DATA.get('access_token_secret')

# VARIABLES

# authentication
auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# pass in authentication to API
api = tweepy.API(auth)

search_term = "stocks" 
tweet_amount = 20

# # testing with public tweets from profile
tweets = api.search_tweets(q=search_term, lang='en')

for tweet in tweets:
    print(tweet.user.screen_name + ': ' + tweet.text)
