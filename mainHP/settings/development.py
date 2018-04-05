from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1o1o1o1o1o1o1o1o1o1o1o1o1o1o1o1o1o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']

WSGI_APPLICATION = 'mainHP.wsgi_dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
INSTALLED_APPS.append('debug_toolbar')
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),
                           os.path.abspath("static"))

INTERNAL_IPS = "127.0.0.1"
