from setuptools import setup

setup(
    name='mainHP',
    version='0.3',
    packages=['lib', 'lib.tests', 'core', 'main', 'main.tests',
              'main.management', 'main.management.commands',
              'tweetable', 'tweetable.tests',
              'transfacils', 'transfacils.tests', 'transfacils.helpers', ],
    url='http://hinatan.jp',
    license='',
    author='kkiyama117',
    author_email='k.kiyama117@gmail.com',
    description='My first server'
)
