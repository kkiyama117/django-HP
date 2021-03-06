from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views
from .forms import LoginForm
from rest_framework import routers
from .api import UserViewSet

app_name = 'account'

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, base_name="user")

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('register_save/', views.register_save, name='register_save'),
    path(
        'login/',
        auth_views.login,
        {'template_name': 'account/login.html',
         'authentication_form': LoginForm},
        name='login'
    ),
    path(
        'logout/',
        auth_views.logout,
        {'template_name': 'account/index.html'},
        name='logout'
    ),
    path('api/', include(router.urls)),
]
