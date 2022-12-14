#!/usr/bin/env bash

# https://www.willianantunes.com/blog/2021/05/production-ready-shell-startup-scripts-the-set-builtin/
set -e

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py seed --create-super-user

python3 manage.py runserver 0.0.0.0:${DJANGO_BIND_PORT:-8000}
