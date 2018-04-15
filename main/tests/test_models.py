import pytest

from main.models import User


@pytest.mark.django_db
class UserTest:
    def setup(self):
        # データを登録しないと表示されないので、事前に登録しておく
        self.user = User.objects.create_user(email="test@test.com",
                                             password="19980117",
                                             first_name="木山", last_name="航平",
                                             tel="00000000000")
        self.user.save()

    def test_add_user(self):
        assert User.objects.all().count() == 1
