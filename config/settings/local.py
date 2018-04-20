from .common import *

ALLOWED_HOSTS = ['localhost']

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware', )
INSTALLED_APPS.append('debug_toolbar', )

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
CELERY_BIN = ".venv/bin/celery"
CELERY_TASK_ALWAYS_EAGER = True
