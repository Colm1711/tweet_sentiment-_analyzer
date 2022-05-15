# Imports

import tweepy
import json
import re

from textblob import TextBlob

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

search_term = "googl" 

# emoji regex search - this was sourced from
pattern = re.compile(
    "(["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "])"
  )

# # testing with public tweets from profile
def get_tweets_from_timeline():
    """
    Description:

    This function fetched the tweets from the homepage of twitter account.

    Params:
            none

    Returns:
            str

    """
    tweets_timeline = api.search_tweets(q=search_term, lang='en')
    return tweets_timeline

# Clean data of retweets, hastags, username handles and hyperlinks
def clean_tweets(tweets_to_clean):
    """
    Description:

    This function cleans the tweets fetched from the homepage of twitter account.

    Params:
            str

    Returns:
            str

    """
    cleaned_tweets = ""
    # string_of_tweets = ""
    for tweet in tweets_to_clean:
        clean_text = tweet.text.replace('RT', '')
        clean_text = clean_text.replace('#', '')
        if clean_text.startswith('@'):
            remove = clean_text.index(' ')
            clean_text = clean_text[remove+2:]
        if clean_text.startswith(' @'):
            remove = clean_text.index(':')
            clean_text = clean_text[remove+2:]
        clean_text = re.sub('http://\S+|https://\S+', '', clean_text)
        clean_text = re.sub(pattern, ' ', clean_text)
    
        cleaned_tweets += clean_text
    return cleaned_tweets

def polarity_analysis(data):
        """
    Description:

    This function scans the cleaned tweets and returns either positive, negative or neutral polarity status.

    Params:
            str

    Returns:
            tuple(float + str)

    """    
    polarity = 0

    analysis = TextBlob(data)
    polarity = analysis.polarity * 10

    if polarity > 1:
        status = 'positive'
    elif polarity < 1:
        status = 'negative'
    else:
        status = 'neutral'

    return polarity, status



