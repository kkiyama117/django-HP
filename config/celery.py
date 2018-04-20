from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
try:
    if os.environ["ENVIRONMENT"] in ("production", "staging"):
        setting = "config.settings.production"
    elif os.environ["DJANGO_SETTINGS_MODULE"] == "config.settings.circleci":
        setting = os.environ["DJANGO_SETTINGS_MODULE"]
except KeyError:
    pass
finally:
    setting = setting if 'setting' in locals() else "config.settings.development"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', setting)

app = Celery('core')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))