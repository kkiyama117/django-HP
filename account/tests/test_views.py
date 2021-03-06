from unittest import TestCase

import pytest

from django.test import RequestFactory
from django.urls import reverse

from account.models import User
from account.views import index, profile


@pytest.mark.django_db
class ViewsTest(TestCase):

    def test_index_with_login_user(self):
        # データを登録しないと表示されないので、事前に登録しておく
        login_user = User.objects.create_user(email="test@test.com",
                                              password="19980117",
                                              first_name="木山", last_name="航平",
                                              tel="00000000000")
        request = RequestFactory().get(reverse('account:index'))
        request.user = login_user
        response = index(request)

        assert response.status_code == 200

    def test_profile(self):
        # データを登録しないと表示されないので、事前に登録しておく
        login_user = User.objects.create_user(email="test@test.com",
                                              password="19980117",
                                              first_name="木山", last_name="航平",
                                              tel="00000000000")
        request = RequestFactory().get(reverse('account:profile'))
        request.user = login_user
        response = profile(request)

        assert response.status_code == 200
        # assert response.data.user == login_user

    def test_register(self):
        # request = RequestFactory().get(reverse('account:register'))
        pass
