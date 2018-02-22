import tweepy
from time import sleep
import os
#from secrets import *

#config variables from Heroku
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search,

    geocode='39.8,-95.583068847656,2500km',
    q='#journojobs OR #journalismjobs OR #mediajobs OR #journojob OR #journalismjobs OR #publicmediajobs OR #pubjobs OR #radiojobs OR "hiring a journalist" OR "new journalism job posting" ').items():
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

        #sleep limits the tweeting to occur every __ seconds - let's try 6 hours between tweets
        sleep(21600)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
