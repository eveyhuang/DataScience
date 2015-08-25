# read in tweets data into a dataframe
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import pandas as pd
tweets = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_15/master/data/so_many_tweets.csv')

from textblob import TextBlob, Word
# use the textblob module to get the sentiment of each
# tweet
<<<<<<< HEAD
def strToSentiment(string):
    return TextBlob(string).sentiment.polarity
    
tweets['Sentiment']=tweets.Text.map(strToSentiment)
=======

from textblob import TextBlob

def stringToSentiment(string):
    return TextBlob(string).sentiment.polarity
    
stringToSentiment('i hate you')
>>>>>>> 764b6887c6a8d030f16bcc42d17a2a5ad91e84d2

tweets['sentiment'] = tweets.Text.map(stringToSentiment)

# Make a column called day which holds the unique
# day it was tweeted, e.g. 5/24/2015
def todate(subject):
    return subject[5:7]+'/'+subject[8:10]+'/'+subject[:4]
tweets['Day']=[todate(i) for i in tweets.Date]

tweets['day'] = tweets.Date.map(lambda x: x[:10])

sent = tweets.groupby('day')['sentiment'].mean()
volume = tweets.groupby('day')['Status'].mean()


sent.plot()

volume.plot()



# For each day, show the number of tweets and
# the average sentiment
sent=tweets.groupby(tweets.Day).Sentiment.mean()
number=tweets.groupby(tweets.Day).Status.count()
# Show a graph of how volume "number of tweets"
# per day changed over the course of May

import matplotlib.pyplot as plt

sent.plot()
number.plot()
# Show a graph of how sentiment of tweets
# changed per day over the course of May
