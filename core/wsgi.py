"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ["ENVIRONMENT"] == "production" or \
        os.environ["ENVIRONMENT"] == "staging":
    setting = "core.settings.production"
elif os.environ["DJANGO_SETTINGS_MODULE"] == "core.settings.circleci":
    setting = os.environ["DJANGO_SETTINGS_MODULE"]
else:
    setting = "core.settings.development"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", setting)

application = get_wsgi_application()
