import factory

from account import models
from django.contrib.auth.hashers import make_password


class UserFactory(factory.Factory):
    class Meta:
        model = models.User

    first_name = factory.Faker('first_name', locale="ja_JP")
    last_name = factory.Faker('last_name', locale="ja_JP")
    email = factory.Faker('email')
    tel = factory.Faker('phone_number')
    password = make_password("pass1234")


class SuperUserFactory(UserFactory):
    class Meta:
        model = models.User

    is_staff = True
    is_superuser = True
