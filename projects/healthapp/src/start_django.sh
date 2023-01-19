#!/usr/bin/env bash

port=8080

python django/myfirstdjango/manage.py migrate
nohup python django/myfirstdjango/manage.py runserver ${port}