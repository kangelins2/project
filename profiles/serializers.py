from django.db import models
from .models import User, Profile
from rest_framework import serializers




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = 'all'


class ProfileDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()