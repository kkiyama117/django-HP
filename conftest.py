"""Pytest のフック
"""
import os
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


@pytest.fixture(scope='module', autouse=True)
def is_omit_test():
    env_test = os.environ.get("DO_ALL_TEST", "False")
    if env_test == "True":
        print("DO_MINIMAL_TEST")
        return False
    elif env_test == "False":
        print("DO_ALL_TEST")
        return True
    else:
        raise ValueError


def pytest_collection_modifyitems(items):
    for item in items:
        item.keywords['django_db'] = pytest.mark.django_db


def pytest_unconfigure(config):
    """pytest の実行時に一度だけ実行される

    """
    subprocess.run(['python', '-Wd', 'manage.py', 'check'], shell=True)
    print("manage.py check done")
