import pytest

from account.factories import UserFactory
from account.models import User
from account.serializer import UserSerializer


@pytest.mark.django_db
class UserTest:
    def setup(self):
        self.serializer = UserSerializer()

    @pytest.mark.parametrize("validated_data", [
        ({
            "email": "test@test.com",
            "password": "password0123",
            "first_name": "きやま",
            "last_name": "こうへい",
            "tel": "08026244315",
        }),
    ])
    def test_create(self, validated_data):
        count_before = User.objects.count()
        user = self.serializer.create(validated_data)
        count = User.objects.count()
        assert count == count_before + 1
        assert user.email == validated_data["email"]
        assert user.tel == validated_data["tel"]

    @pytest.mark.parametrize("validated_data", [
        ({
            "email": "test@test.com",
            "password": "pass0123word",
            "first_name": "きやま",
            "last_name": "こうへい",
            "tel": "08026244315",
        }),
    ])
    def test_update(self, validated_data):
        user = UserFactory()
        user_new = self.serializer.update(user, validated_data)
        assert user_new.email == validated_data["email"]
        assert user_new.tel == validated_data["tel"]
        assert user_new.password == validated_data["password"]
