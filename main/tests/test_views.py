from unittest import TestCase

import pytest

from django.test import RequestFactory
from django.urls import reverse

from main.models import User
from main.views import index, user


@pytest.mark.django_db
class ViewsTest(TestCase):

    def test_index(self):
        # データを登録しないと表示されないので、事前に登録しておく
        login_user = User.objects.create_user(email="test@test.com",
                                              password="19980117",
                                              first_name="木山", last_name="航平",
                                              tel="00000000000")
        request = RequestFactory().get(reverse('main:index'))
        request.user = login_user
        response = index(request)

        assert response.status_code == 200

    def test_user(self):
        # データを登録しないと表示されないので、事前に登録しておく
        login_user = User.objects.create_user(email="test@test.com",
                                              password="19980117",
                                              first_name="木山", last_name="航平",
                                              tel="00000000000")
        request = RequestFactory().get(reverse('main:user'))
        request.user = login_user
        response = user(request)

        assert response.status_code == 200
