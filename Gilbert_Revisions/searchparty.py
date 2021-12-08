from t import twitter_auth
import pandas as pd
import tweepy
from datetime import datetime

def searchparty(keyword, date, max_number):
    auth=twitter_auth()
    api=tweepy.API(auth)
    num=0
    tweets=[]

    for tweet in tweepy.Cursor(api.search_tweets, q=keyword, lang="en", until=date, tweet_mode='extended').items(max_number):
        num=num+1
        hashtags = tweet.entities['hashtags']
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text=tweet.full_text
        hashtext=list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])

        tweets.append(text)
    return(tweets)
  
      
#if __name__ == '__main__':   
#    auth=twitter_auth()
#    api=tweepy.API(auth)



#Resources used
# https://www.geeksforgeeks.org/extracting-tweets-containing-a-particular-hashtag-using-python/
# https://docs.tweepy.org/en/stable/api.html#tweets
# https://docs.tweepy.org/en/stable/client.html#tweets
#


