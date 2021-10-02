#!/bin/bash

sleep 2

python3 manage.py migrate

python3 manage.py load_cities

python3 manage.py load_forecast

python3 manage.py runserver 0.0.0.0:8000

