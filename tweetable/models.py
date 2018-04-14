from django.db import models


class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    user_name = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=30)


class Tweet(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    context = models.CharField(max_length=140)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
