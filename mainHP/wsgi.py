"""
WSGI config for mainHP project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ["ENVIRONMENT"] == "production" or\
        os.environ["ENVIRONMENT"] == "staging":
    setting = "mainHP.settings.production"
else:
    setting = "mainHP.settings.development"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", setting)

application = get_wsgi_application()
