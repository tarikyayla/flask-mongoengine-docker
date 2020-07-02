import requests 
from celery import Celery
import os 


CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

celery.conf.beat_schedule = {
  'task-reminder': {
    'task': 'reminder',
    'schedule': 60.0, # 60 saniyede bir 
  },
}

@celery.task(name="reminder")
def reminder():
  requests.get("https://web:5000/task-reminder",verify=False)