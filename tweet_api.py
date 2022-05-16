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
    # have set language to english and limited the search to first 200
    tweets_timeline = api.search_tweets(q=search_term, lang='en', count=2000, tweet_mode='extended')
    return tweets_timeline


# Clean data of retweets, hastags, username handles and hyperlinks
def clean_tweets(tweets_to_clean):
    """
    Description:

    This function cleans the tweets fetched from the homepage of twitter account.

    Params:
            str

    Returns:
            list(str's)

    """
    # list to populate cleaned tweets
    tweet_list = []

    tweets_dict = {tweet.full_text for tweet in tweets_to_clean}
    for tweet in tweets_dict:
        # removing retweets from tweets
        clean_text = tweet.replace('RT', '')
        # removing new line chars from tweets
        clean_text = clean_text.replace('\n', '')
        # removing hashtags from tweets
        clean_text = clean_text.replace('#', '')
        # removing twitter handles from tweets
        if clean_text.startswith('@'):
            remove_at = clean_text.index(' ')
            clean_text = clean_text[remove_at+2:]
        # removing twitter hanldes with leading spaces
        if clean_text.startswith(' @'):
            remove_space_at = clean_text.index(':')
            clean_text = clean_text[remove_space_at+2:]
        # removing any links
        clean_text = re.sub('http://\S+|https://\S+', '', clean_text)
        # removing any emojis, the list was sourced externally. Ref in README file.
        clean_text = re.sub(pattern, ' ', clean_text)
        tweet_list.append(clean_text)
    return tweet_list

def polarity_analysis(data):
    """
    Description:

    This function scans the cleaned tweets and returns either positive, negative or neutral polarity status.

    Params:
        list(str)

    Returns:
        f string of string data

    """   
 
    polarity = 0
    positive = 0
    negative = 0
    neutral = 0
    # unpacks list for individual tweets
    for tweet in data:
        # creating textblob object for analysis
        analysis = TextBlob(tweet)
        # using in built func to analyze polarity of each tweet
        tweet_data_polarity = analysis.polarity
        # assigning positive, negative or neutral based on polarity score
        if tweet_data_polarity > 0:
            positive += 1
        elif tweet_data_polarity < 0:
            negative += 1
        else:
            neutral += 1
        polarity += analysis.polarity
    return f'Polarity: {polarity}\nAmount of positive: {positive}\nAmount of negative: {negative}\nAmount of neutral: {neutral}'

