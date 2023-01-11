from polls.models import Choice, Question  # Import the model classes we just wrote.
import datetime

# No questions are in the system yet.
Question.objects.all()

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
from django.utils import timezone

q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
q.save()

# Now it has an ID.
q.id

# Access model field values via Python attributes.
q.question_text
q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=datetime.timezone.utc)

# Change values by changing the attributes, then calling save().
q.question_text = "What's up?"
q.save()

# objects.all() displays all the questions in the database.
Question.objects.all()

q = Question.get(id=1)
q.was_published_recently()  # methode opgesteld als onderdeel van class Question


q.choice_set.create(choice_text="The sky", votes=0)

c = q.choice_set.create(choice_text="Just hacking again", votes=0)
