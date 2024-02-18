from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

