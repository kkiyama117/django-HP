#!/usr/bin/env python
import os
import sys

try:
    if os.environ["ENVIRONMENT"] in ("production", "staging"):
        setting = "mainHP.settings.production"
except KeyError:
    pass
finally:
    setting = setting if 'setting' in locals() else "mainHP.settings.development"

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", setting)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
