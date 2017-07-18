from django.conf.urls import url
from .views import get_tweets, show_tweets, tweets_data ,index

urlpatterns = [
    url(r'^get', get_tweets, name='get_tweets'),
    url(r'^show', show_tweets, name='show_tweets'),
    url(r'^data', tweets_data, name='tweets_data'),
]