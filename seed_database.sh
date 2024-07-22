#!/bin/bash

rm db.sqlite3
rm -rf ./horseapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations horseapi
python3 manage.py migrate horseapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

