import json
import time

from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from celery.result import AsyncResult

from .models import Tweet, TwitterUser
from .tasks import check_username


class GetTweetsView(generic.DetailView):
    def post(self, request):
        twitter_user = request.POST.get("twitterUser").lower()
        clean_twitter_user = twitter_user.replace("@", "")
        twitter_get = check_username(clean_twitter_user)

        if twitter_get == "User not found.":
            messages.add_message(request, messages.ERROR, twitter_get)
            return redirect('home')

        searched_users = request.user.searched_users
        if clean_twitter_user not in searched_users:
            request.user.searched_users.append(clean_twitter_user)
            request.user.save()

        time.sleep(5)

        return redirect(reverse('show_tweets') + '?username=' + clean_twitter_user)


class ShowTweetsView(generic.DetailView):
    template_name = 'show_tweets.html'

    def get(self, request):
        searched_users = request.user.searched_users
        twitter_user = TwitterUser.objects.get(username=request.GET.get('username'))
        all_tweets = Tweet.objects.filter(username=twitter_user)
        return render(request, self.template_name, {'searched_users': searched_users,
                                                    'twitter_user': twitter_user})


class TweetsDataView(generic.DetailView):
    def get(self, request):
        twitter_user = TwitterUser.objects.get(username=request.GET.get('username'))
        all_tweets = Tweet.objects.filter(username=twitter_user)
        data = []
        for tweet in all_tweets:
            data.append(eval(tweet.data))
        return JsonResponse(data, safe=False, json_dumps_params={'indent': 4, 'ensure_ascii': False})
