#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python the_weather/manage.py collectstatic --no-input
python the_weather/manage.py migrate
