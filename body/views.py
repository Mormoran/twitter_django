from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import request
from .pull_tweets import twitter_logic, get_mongo_collections, get_tweets_json


def index(request):
    return render(request, 'index.html')


# The following views all get the tweets from twitter, send the JSONed data to a data page and then show the tweets in graph form


# Gets the screen_name from the URL and connects to twitter to retrieve the data, and returns a URL redirect
# with show_tweets/?screen_name=<the screen name> which triggers urls.py on a url change
# @login_required(login_url='/accounts/login')
def get_tweets(request):
    screen_name = request.GET['screen_name']
    screen_name = screen_name.lower()
    twitter_logic(screen_name)
    return redirect(reverse('show_tweets') + '?screen_name=' + screen_name)  

# Stores all tweet JSONed data on a separate URL for graphs.js to retrieve and build the SVGs, retrieving the user_name from the URL
# to connect to the corret collection in MongoDB
def tweets_data(request):
    screen_name = request.GET['screen_name']
    screen_name = screen_name.lower()    
    return HttpResponse(get_tweets_json(screen_name))

# Gets all collections from MongoDB and stores them in coll using a function, to populate the selection form. It returns it in 
# dictionary format using Django's way of passing variables to the HTML
def show_tweets(request):
    screen_name = request.GET['screen_name']
    coll = get_mongo_collections()
    return render(request, 'done.html', {'screen_name': screen_name, 'coll': coll})