from lib import utils
from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1o1o1o1o1o1o1o1o1o1o1o1o1o1o1o1o1o'

env = utils.get_data_from_env("circleci")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']

WSGI_APPLICATION = 'core.wsgi.application'
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "circle_test",
        'USER': "root",
        'PASSWORD': "",
        'HOST': "postgres://root@127.0.0.1:5432/circle_test?sslmode=disable",
        'PORT': '5432',
    }
}
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),
                           os.path.abspath("static"))

# celery
CELERY_BIN = "venv/bin/celery"
CELERY_TASK_ALWAYS_EAGER = True
