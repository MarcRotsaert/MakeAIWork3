from django.apps import AppConfig
import logging

logging.basicConfig(level="DEBUG")


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
