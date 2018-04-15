from django.urls import path, include
from rest_framework import routers

from tweetable.api import UserViewSet, TweetViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'statues', TweetViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
