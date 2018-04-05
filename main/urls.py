from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views
from .forms import LoginForm
from rest_framework import routers
from .api import UserViewSet

app_name = 'main'

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, base_name="user")

urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.user, name='user'),
    path('register', views.register, name='register'),
    path('register_save', views.register_save, name='register_save'),
    path(
        'login',
        auth_views.login,
        {'template_name': 'main/login.html',
         'authentication_form': LoginForm},
        name='login'
    ),
    path(
        'logout',
        auth_views.logout,
        {'template_name': 'main/index.html'},
        name='logout'
    ),
    path('api/', include(router.urls)),
]
