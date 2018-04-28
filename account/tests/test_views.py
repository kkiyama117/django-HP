import pytest

from django.test import TestCase, RequestFactory
from django.urls import reverse

from account.models import User
from account.views import index, profile, register, register_save


@pytest.mark.django_db
class ViewsTest(TestCase):

    def test_index_with_login_user(self):
        # データを登録しないと表示されないので、事前に登録しておく
        login_user = User.objects.create_user(email="test@test.com",
                                              password="19980117",
                                              first_name="木山", last_name="航平",
                                              tel="00000000000")
        self.client.login(username=login_user.email, password="19980117")
        response = self.client.get(reverse('account:index'))
        assert response.status_code == 200

    def test_profile(self):
        # データを登録しないと表示されないので、事前に登録しておく
        login_user = User.objects.create_user(email="test@test.com",
                                              password="19980117",
                                              first_name="木山", last_name="航平",
                                              tel="00000000000")
        self.client.login(username=login_user.email, password="19980117")
        response = self.client.get(reverse('account:profile'))
        # self.assertTemplateUsed(response, 'account/profile.html')
        assert response.status_code == 200

    def test_register(self):
        response = self.client.get(reverse('account:register'))
        assert response.status_code == 200
