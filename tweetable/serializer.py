# coding: utf-8
from rest_framework import serializers

from .models import User, Tweet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TweetSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Tweet
        fields = '__all__'

