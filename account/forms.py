from django.contrib.auth.forms import UserChangeForm, UserCreationForm, \
    AuthenticationForm

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


class RegisterForm(MyUserCreationForm):
    """User create form"""
    pass


class LoginForm(AuthenticationForm):
    """User login form"""
    pass
