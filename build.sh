#!/bin/bash

#bulid the project
echo "Build the project..."
python -m pip install -r requirements.txt

echo "Made Migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect Static..."
python manage.py collectstatic --noinput --clear