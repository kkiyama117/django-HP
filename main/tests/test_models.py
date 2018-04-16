import pytest

from main.models import User


@pytest.mark.django_db
class UserTest:
    def setup(self):
        # データを登録しないと表示されないので、事前に登録しておく
        self.super_user = User.objects.create_user(
            email="k.kiyama117@gmail.com",
            password="password0123",
            first_name="木山",
            last_name="航平",
            tel="08026244315")
        self.super_user.save()

    def test_add_user(self):
        assert User.objects.all().count() == 1
