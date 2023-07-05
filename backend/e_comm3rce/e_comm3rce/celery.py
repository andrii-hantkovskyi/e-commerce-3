import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_comm3rce.settings')

app = Celery('e_comm3rce')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.update(timezone=settings.TIME_ZONE)
app.conf.beat_schedule = {
    'send-every-day-noon': {
        'task': 'waitings.tasks.send_mails_for_waiting_users',
        'schedule': crontab(hour='12', minute='21'),
    },
}
