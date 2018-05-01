#!/usr/bin/python
from setuptools import setup

setup(
    name='mainHP',
    version='0.4.1',
    description='kkiyama117\'s homepage',
    author='kkiyama117',
    author_email='k.kiyama117@gmail.com',
    packages=['lib', 'lib.tests', 'config', 'account', 'account.tests',
              'account.management', 'account.management.commands',
              'tweetable', 'tweetable.tests',
              'transfacils', 'transfacils.tests', 'transfacils.helpers',
              'unimap', "unimap.tests"],
    url='http://hinatan.jp',
    license='', install_requires=['django-model-utils']
)
