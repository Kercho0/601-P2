
import sys
import tweepy

def twitter_auth():
	try:
		consumer_key='W0LYYtoUzhAzmA9ZDc6lb8sCa'
		consumer_secret='qVlY2PQiMLt934RUVX8t05DAKmVPJOwiFYh8fI25bMGWaGebqA'
		access_token='933749117360201728-K0Q4DlEIf61LzGmQQWgiERaWX1BOZVJ'
		access_secret='UIuHAyRYzsn50VkpdB9dzBfUg0bW8bdrEIffT7qDSX28c'
	except KeyError:
		sys.stderr.write("TWITTER_* environment variable not set \n")
		sys.exit(1)

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	return auth
    