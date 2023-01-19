# Debian Base Image with Python 3.11
FROM python:bullseye

# Environment variables
ENV PYTHONBUFFERED=1
ENV DJANGO_SETTINGS_MODULE="myfirstdjango.settings"

# Copy sources
ADD src /app

# Install Pyton libraries
RUN python -m pip install --no-cache-dir -r /app/install/requirements.txt 

# Filepath location in Docker container
WORKDIR /app

# Expose Django port
EXPOSE 8080

ENTRYPOINT ["python", "django/myfirstdjango/manage.py", "runserver", "0.0.0.0:8080"]