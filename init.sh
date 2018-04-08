#!/bin/bash
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py initializer
python manage.py loaddata initial_data.json
