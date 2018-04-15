import pytest
from django.core.exceptions import ValidationError
from django.test import TestCase
from tweetable.models import User


@pytest.mark.tweetable
@pytest.mark.models
@pytest.mark.django_db
class UserModelTest:
    @pytest.mark.parametrize("test_name, test_user_name", [
        ("test1", "test11"),
        ("test2", "二個目マン"),
        pytest.param("6*9", ("a" * 100),
                     marks=pytest.mark.xfail),
        pytest.param(("a" * 100), "test",
                     marks=pytest.mark.xfail),
    ])
    def test_field_with_no_error(self, test_name, test_user_name):
        model = User(id=100, name=test_name, user_name=test_user_name)
        try:
            model.full_clean()
        except ValidationError as e:
            pytest.fail()
            print(e)

    @pytest.mark.parametrize("test_name, test_user_name", [
        pytest.param("6*9", ("a" * 100), ),
        pytest.param(("a" * 100), "test", ),
    ])
    def test_field_with_error(self, test_name, test_user_name):
        model = User(id=100, name=test_name, user_name=test_user_name)
        with pytest.raises(ValidationError):
            model.full_clean()
