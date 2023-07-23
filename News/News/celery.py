import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News.settings')

app = Celery('News')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_notification_every_monday_8am': {
        'task': 'news.tasks.weekly_newsletter',
        'schedule': 10,
        }
    }

