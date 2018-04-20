"""Pytest のフック
"""
import subprocess

# -*- coding: utf-8 -*-
import django_webtest
import pytest


@pytest.fixture(scope='function')
def app(request):
    """ Webtest の時に使う
    Args:
        request:

    Returns:

    """
    wtm = django_webtest.WebTestMixin()
    wtm._patch_settings()
    request.addfinalizer(wtm._unpatch_settings)
    return django_webtest.DjangoTestApp()


def pytest_collection_modifyitems(items):
    for item in items:
        item.keywords['django_db'] = pytest.mark.django_db


def pytest_unconfigure(config):
    """pytest の実行時に一度だけ実行される

    """
    subprocess.run(['python', '-Wd', 'manage.py', 'check'], shell=True)
