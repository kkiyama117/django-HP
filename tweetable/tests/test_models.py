import pytest
from django.test import TestCase


@pytest.mark.django_db
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)
