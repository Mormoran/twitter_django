from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models


class CustomUser(AbstractUser):
    searched_users = ArrayField(models.CharField(max_length=15, blank=False))

    def __str__(self):
        return self.username
