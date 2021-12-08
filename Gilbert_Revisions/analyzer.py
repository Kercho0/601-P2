from t import twitter_auth
from searchparty import searchparty
import pandas as pd
import tweepy
import datetime
import sys
# from datetime import datetime
from classify import classify
from sentiment import sentiment


def analyzer(keyword, date, number):
    texts=[]
    texts = searchparty(keyword, date, number)
    sentiments=[]
    contents=[]

    if not texts:
        print ("Couldn't find any tweets matching your search")
    
    else: 

        for i in range(len(texts)):
            sentiments.append(float(sentiment(texts[i])))
            contents.append(classify(texts[i]))
        avg_sentiment=0
        for i in range(len(sentiments)):
            avg_sentiment=avg_sentiment+sentiments[i]
    
        print("Average sentiment: ", avg_sentiment)
        print("Content Categories: ")
        for i in range (len(contents)):
            print(contents[i])
            


