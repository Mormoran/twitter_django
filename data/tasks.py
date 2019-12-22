import json
import pprint

from django.conf import settings

import tweepy
from celery.decorators import task
from decouple import config

from .models import Tweet, TwitterUser


# Script to download up to <= 3200 (the official Twitter API limit) of most recent tweets from a user's timeline
class TwitterHarvester(object):
	"""Create a new TwitterHarvester instance"""
	def __init__(self, consumer_key, consumer_secret,
				 access_token, access_token_secret,
				 wait_on_rate_limit=False,
				 wait_on_rate_limit_notify=False):

		self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		self.auth.secure = True
		self.auth.set_access_token(access_token, access_token_secret)
		self.__api = tweepy.API(self.auth,
								wait_on_rate_limit=wait_on_rate_limit,
								wait_on_rate_limit_notify=wait_on_rate_limit_notify)

	@property
	def api(self):
		return self.__api

# Instantiate an object of TwitterHarvester to use it's api object
# make sure to set the corresponding flags as True to whether or
# not automatically wait for rate limits to replenish
a = TwitterHarvester(settings.CONSUMER_KEY, settings.CONSUMER_SECRET,
						settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET,
						wait_on_rate_limit=True,
						wait_on_rate_limit_notify=True)
api = a.api

@task(name="check_username")
def check_username(username):
	try:
		user = api.get_user(username)
	except tweepy.error.TweepError:
		return "User not found."

	twitter_user = TwitterUser.objects.get_or_create(username=username)[0]

	twitter_logic.delay(username)
	return "Success."

@task(name="get_tweets")
def twitter_logic(username):
	# Use the cursor to skip the handling of the pagination mechanism
	# http://docs.tweepy.org/en/latest/cursor_tutorial.html
	tweets = tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended").items()

	twitter_user = TwitterUser.objects.get(username=username)

	while True:
		# As long as I still have a tweet to grab
		try:
			data = tweets.next()
		# When the cursor objects reaches the end, do a bulk insert into the DB to save time
		except StopIteration:
			break

		# with open("data.json", "a") as data_file:
		# 	data_file.write(json.dumps(data._json, indent=4, sort_keys=True))

		if "retweeted_status" in data._json.keys():
			data._json['retweeted'] = True
		else:
			data._json['retweeted'] = False

		if data._json['entities']['hashtags']:
			data._json['has_hashtags'] = True
		else:
			data._json['has_hashtags'] = False

		# Using update_or_create since a tweet's data changes over time (people retweet, like, favourite)
		# The username and created_at kwargs are using for filtering whether the objects instance exists or not
		# while the defaults takes a dict with the object attributes we wish to update.
		tweet = Tweet.objects.update_or_create(username=twitter_user, created_at=data.created_at, defaults={'data': data._json})