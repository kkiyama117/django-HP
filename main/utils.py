from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, \
    AuthenticationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'tel',)


class MyAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'tel')
