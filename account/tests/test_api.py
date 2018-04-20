import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from account.api import UserViewSet
from account.factories import UserFactory, SuperUserFactory
from account.models import User
from account.serializer import UserSerializer


class UserAPITest(APITestCase):
    @pytest.mark.django_db
    def test_getList(self):
        user = UserFactory.build()
        user.save()
        superuser = SuperUserFactory.build()
        superuser.save()
        client = APIClient()
        client.login(email=user.email,
                     password="pass1234")
        data = {"pk": str(user.id)}
        url = reverse('account:user-detail', kwargs=data)
        # url = reverse('account:user-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        users = User.objects.all_for_instance(user)
        # check user queryset
        assert users.count() is 1
        serializer = UserSerializer(users, many=True)
        # View and Serializer test
        assert response.data in serializer.data
