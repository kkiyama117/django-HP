from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1o1o1o1o1o1o1o1o1o1o1o1o1o1o1o1o1o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),
                           os.path.abspath("static"))

INTERNAL_IPS = "127.0.0.1"

# celery
CELERY_BIN = "venv/bin/celery"
CELERY_TASK_ALWAYS_EAGER = True
