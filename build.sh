#!/bin/bash

#bulid the project
echo "Build the project..."
python3.8 -m pip install -r requirements.txt

echo "Made Migration..."
python3.8 manage.py makemigrations --noinput
python3.8 manage.py migrate --noinput

echo "Collect Static..."
python3.8 manage.py collectstatic --noinput --clear