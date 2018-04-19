import pytest
from faker import Faker

from account.forms import MyUserCreationForm


class UserFormTest:
    @pytest.mark.parametrize(('email', 'tel', 'password1', 'password2'), [
        ('test1@test.com', "00000000000", 'pass1234', "pass1234"),
        (Faker().email(), "00000000001", 'pass1234', "pass1234"),
        pytest.param("", "01010100101", "pass1234", "pass1234",
                     marks=pytest.mark.xfail),
        pytest.param("test@test.com", "01010100111111", "pass1234", "pass1234",
                     marks=pytest.mark.xfail),
        pytest.param("test@test.com", "01011112222", "pass1234", "pass12345",
                     marks=pytest.mark.xfail),
    ])
    def test_my_user_creation_form_valid(self, email, tel, password1,
                                         password2):
        form = MyUserCreationForm(
            data={'email': email, 'tel': tel, 'password1': password1,
                  'password2': password2})

        assert form.is_valid()
