import sys
import tweepy
from t import twitter_auth


def get_twitter_client():
	auth=twitter_auth()
	client=tweepy.API(auth, wait_on_rate_limit=True)
	return client

if __name__ == '__main__':
	user = input ("Enter Username: ")
	client = get_twitter_client()
	for status in tweepy.Cursor(client.user_timeline, screen_name=user).items(25):
		print(status.text)