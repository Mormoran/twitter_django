from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models

def default_array():
    return []

class CustomUser(AbstractUser):
    searched_users = ArrayField(models.CharField(max_length=15, blank=False), null=True, blank=True, default=default_array)

    def __str__(self):
        return self.username
