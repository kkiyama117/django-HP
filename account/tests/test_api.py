from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class UserAPITest(APITestCase):
    def test_getList(self):
        url = reverse('user-list')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
