import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')
broker_url = 'amqp://guest:guest@0.0.0.0:5672//'

app = Celery('config')
app.config_from_object('django.conf:settings',namespace='CELERY')

app.autodiscover_tasks()