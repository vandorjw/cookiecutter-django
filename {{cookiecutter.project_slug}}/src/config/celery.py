# http://docs.celeryproject.org/en/v4.1.0/django/first-steps-with-django.html
import os
from celery import Celery
from kombu import Exchange, Queue

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('{{cookiecutter.project_name}}')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

default_exchange = Exchange('default', type='direct')
urgent_exchange = Exchange('urgent', type='direct')

app.conf.task_queues = (
    Queue('default', default_exchange, routing_key='default'),
    Queue('urgent', urgent_exchange, routing_key='urgent'),
)
app.conf.task_default_queue = 'default'
app.conf.task_default_exchange = 'default'
app.conf.task_default_routing_key = 'default'


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
