
import sys
import tweepy

def twitter_auth():
	try:
		consumer_key='<ENTRER CONSUMER KEY HERE>'
		consumer_secret='<ENTER CONSUMER SECRET KEY HERE>'
		access_token='<ENTER ACCESS TOKEN HERE>'
		access_secret='<ENTER SECRET ACCESS TOKEN HERE>'
	except KeyError:
		sys.stderr.write("TWITTER_* environment variable not set \n")
		sys.exit(1)

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	return auth
