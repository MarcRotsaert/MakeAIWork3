echo "yes"
python django/myfirstdjango/manage.py runserver &
sleep 10
start msedge.exe http://localhost:8000/polls/happ

