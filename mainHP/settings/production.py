from environ import environ

from .common import *

env = environ.Env()
env_base=environ.Path(__file__) - 3
if os.environ["ENVIRONMENT"] == "staging":
    env_file = str(env_base.path(".env/staging"))
else:
    env_file = str(env_base.path(".env/production"))
env.read_env(env_file)

SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '133.130.113.34.xip.io', '13.250.165.215.xip.io']

WSGI_APPLICATION = 'mainHP.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASS"),
        'HOST': env("DB_HOST"),
        'PORT': '5432',
    }
}

STATIC_ROOT = '/static/'

REST_FRAMEWORK.update({
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
})
