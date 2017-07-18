from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import request
from .pull_tweets import twitter_logic, get_mongo_collections, get_tweets_json


def index(request):
    return render(request, 'index.html')


def show_tweets(request):
    screen_name = request.GET['screen_name']
    coll = get_mongo_collections()
    return render(request, 'done.html', {'screen_name': screen_name, 'coll': coll})


# @login_required(login_url='/accounts/login')
def get_tweets(request):
    screen_name = request.GET['screen_name']
    screen_name = screen_name.lower()
    twitter_logic(screen_name)
    return redirect(reverse('show_tweets') + '?screen_name=' + screen_name)  


def tweets_data(request):
    screen_name = request.GET['screen_name']
    screen_name = screen_name.lower()    
    return HttpResponse(get_tweets_json(screen_name))