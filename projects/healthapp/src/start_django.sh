#!/usr/bin/env bash

port=8080

(cd django/myfirstdjango; nohup python manage.py runserver ${port} &)
sleep 7
python -m webbrowser -t "http://localhost:${port}/polls/happ" 

