from django.db import models


class TwitterUser(models.Model):
    username = models.CharField(max_length=15)

    def __str__(self):
        return self.username

    class Meta:
        unique_together=(('username'),)


class Tweet(models.Model):
    username = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    data = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        unique_together=(('username', 'created_at'),)
