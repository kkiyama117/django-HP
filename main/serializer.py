# coding: utf-8
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if not isinstance(instance, User):
            raise ValueError("Instance is not User class")
        if "password" in validated_data:
            validated_data["password"] = make_password(
                validated_data["password"])
        return super(UserSerializer, self).update(instance, validated_data)
