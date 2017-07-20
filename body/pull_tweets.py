# Obtained from https://gist.github.com/MihaiTabara/631ecb98f93046a9a454
# Modified by Andres Correa with help from Richard Dalton

# Script to download up to <= 3200 (the official Twitter API limit) of most recent tweets from a user's timeline

import os
from pymongo import MongoClient
from flatten_json import flatten
from bson import json_util
import tweepy
import json
from twitter_django.env import *
from django.conf import settings




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




def twitter_logic(user_name):
    # Instantiate an object of TwitterHarvester to use it's api object
    # make sure to set the corresponding flags as True to whether or 
    # not automatically wait for rate limits to replenish
    a = TwitterHarvester(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, 
                         settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET,
                         wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)
    api = a.api

    # Assume there's MongoDB running on the machine, get a connection to it
    MONGODB_URI = os.environ.get('MONGODB_URI')
    # conn = MongoClient('localhost', 27017)
    conn = MongoClient(MONGODB_URI)
    db = conn['twitter_db']
    user_name = user_name.lower()
    collection = db[user_name]

    # Use the cursor to skip the handling of the pagination mechanism 
    # http://docs.tweepy.org/en/latest/cursor_tutorial.html
    tweets = tweepy.Cursor(api.user_timeline, screen_name=user_name).items()

    while True:

        # As long as I still have a tweet to grab
        try:
            data = tweets.next()
        except StopIteration:
            break

        # Convert from Python dict-like structure to JSON format
        jsoned_data = json.dumps(data._json)
        tweet = json.loads(jsoned_data)

        tweet = flatten(tweet)

        print(tweet['user_screen_name'] + " - " + tweet['created_at'] + ": " + tweet['text'])

        # Insert the information in the database
        if collection.find({'id': tweet['id']}).count() == 0:
            collection.insert(tweet)
            collection.update_many({'entities_hashtags_0_text': {'$exists': True}}, {'$set': {'has_hashtags': True}})
            collection.update_many({'entities_hashtags_0_text': {'$exists': False}}, {'$set': {'has_hashtags': False}})

            collection.update_many({'retweeted_status_id': {'$exists': True}}, {'$set': {'is_retweet': True}})
            collection.update_many({'retweeted_status_id': {'$exists': False}}, {'$set': {'is_retweet': False}})
        else:
            collection.update_one({'id': tweet['id']}, {'$set': {'retweet_count': tweet['retweet_count'], 'favorite_count': tweet['favorite_count'], 'favorited': tweet['favorited'], 'retweeted': tweet['retweeted']}}, upsert=False)




# Connect to MongoDB, and store all collections in a list object that is used in a for loop in the HTML to populate the select dropdown
def get_mongo_collections():
    conn = MongoClient('localhost', 27017)
    database = conn['twitter_db']
    collections = database.collection_names(include_system_collections=False)

    # Sort collection alphabetically
    collections = sorted(collections)
    return collections



# Connect to MongoDB using the screen_name we retrieve from the URL (through views.py) to access the collection we want
def get_tweets_json(screen_name):
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    DBS_NAME = 'twitter_db'
    COLLECTION_NAME = screen_name

    # Define the record fields that we wish to retrieve from our MongoDB collection.
    FIELDS = {
        '_id': False,
        'id_str': True, # ID number of the tweet in Str type, to form complete tweet url: "https://twitter.com/" + scr + "/status/" + id_str
        'created_at': True,
        'text': True,
        'entities_urls_0_expanded_url': True,
        'in_reply_to_screen_name': True,
        'user_screen_name': True,
        'geo': True,
        'coordinates': True,
        'place': True,
        'retweet_count': True,
        'favorite_count': True,
        'has_hashtags': True,
        'is_retweet': True,
        'entities_hashtags_0_text': True,
        'entities_hashtags_1_text': True,
        'entities_hashtags_2_text': True,
        'entities_hashtags_3_text': True,
        'user_profile_image_url': True,
    }

    # Open a connection to MongoDB using a with statement such that the
    # connection will be closed as soon as we exit the with statement
    with MongoClient(MONGODB_HOST, MONGODB_PORT) as conn:

        # Define which collection we wish to access
        collection = conn[DBS_NAME][COLLECTION_NAME]

        # Retrieve a result set only with the fields defined in FIELDS
        # and limit the the results to 55000

        the_tweets = collection.find(projection=FIELDS)

        # Convert projects to a list in a JSON object and return the JSON data
        return json.dumps(list(the_tweets))