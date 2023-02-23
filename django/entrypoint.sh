#!/bin/bash

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn to_do_list.wsgi --reload --bind  0.0.0.0:8000