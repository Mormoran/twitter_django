from django.urls import path, re_path

from . import views


urlpatterns = [
    path('get/', views.GetTweetsView.as_view(), name='get_tweets'),
    path('show/', views.ShowTweetsView.as_view(), name='show_tweets'),
    path('data/', views.TweetsDataView.as_view(), name='tweet_data'),
]