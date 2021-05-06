import tweepy as tw
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler #authenticating based on credentials
from tweepy import Stream
from textblob import TextBlob
import datetime
import csv
import re
import numpy as np
import pandas as pd

#My Keys
consumer_key= '##########################'
consumer_secret= '##########################'
access_token= '##########################'
access_token_secret= '##########################'

#Authentication
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)

#break up tweet and only keep the text part
def segment_tweet(tweet, default_value=None):
    data = {}
    data['tweet'] = clean_tweet(tweet.full_text) if clean_tweet(tweet.full_text) else default_value #clean the text of the tweet
    return data

#analyze sentiment using text blob 
def analyze_sentiment(tweet):
        analysis = TextBlob(clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
           return 1 #positive sentiment 
        elif analysis.sentiment.polarity == 0: 
           return 0 #neutral sentiment
        else:
           return -1 #negative sentiment

#clean tweets to get accurate sentiment 
def clean_tweet(tweet):
    #cleaning twwets
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove links
    tweet = " ".join(tweet.split())
    tweet = tweet.replace("#", "").replace("_", " ") #Remove hashtag sign but keep text
    return tweet


#keywords
search_words = "Joe Biden OR potus OR President of the United States OR Biden"
search_query = search_words + " -filter:retweets AND -filter:replies" #filter out retweets
#first collect tweets
#tweets = collectTweets()
tweets = [segment_tweet(tweet) for tweet in tw.Cursor(api.search,
                       q=search_query,
                       lang="en",
                       result_type="recent",
                       include_entities= True,
                       tweet_mode="extended",
                       monitor_rate_limit=True,
                       wait_on_rate_limit=True).items(50)] #so that it ends 


#ceate database of tweets
df = pd.DataFrame(tweets)
#analyze sentiment
df['sentiment'] = np.array([analyze_sentiment(tweet) for tweet in df['tweet']])

#print(df.head(20)) #for debugging purposes

#convert database to CSV
df.to_csv('bidenTweets.csv', sep = ',', index = None, header=True)
