from t import twitter_auth
import pandas as pd
import tweepy
from datetime import datetime

def searchparty(keyword, date, max_number):
	num=0
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

		print()
		print(f"Tweet {num}: ")
		print(f"Username: {tweet.user.screen_name}")
		print(f"Description: {tweet.user.description}")
		print(f"Location: {tweet.user.location}")
		print(f"Following Count: {tweet.user.friends_count}")
		print(f"Follower Count: {tweet.user.followers_count}")
		print(f"Total Tweets: {tweet.user.statuses_count}")
		print(f"Retweet Count: {tweet.retweet_count}")
		print(f"Tweet Text: {text}")
		print(f"Hashtags Used: {hashtext}")
  
      
if __name__ == '__main__':   
    auth=twitter_auth()
    api=tweepy.API(auth)
    keyword= input("Enter keyword to search for: ")

    today=datetime.today().strftime('%Y-%m-%d')
    
    input_date=input("Enter Date (yyyy-mm-dd, press enter for today): ")
    
    max_number=int(input("Number of tweets to retrieve: ") )    
    if input_date == '':
        today = today
    else:
        today = input_date
    searchparty(keyword, today, max_number)


#Resources used
# https://www.geeksforgeeks.org/extracting-tweets-containing-a-particular-hashtag-using-python/
# https://docs.tweepy.org/en/stable/api.html#tweets
# https://docs.tweepy.org/en/stable/client.html#tweets
#





