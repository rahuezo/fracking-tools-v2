from __future__ import absolute_import, unicode_literals
from celery import Celery

import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fracking_tools.settings')
os.environ['SNER_ROOT'] = '/home/rudy/fracking-tools-v2/fracking_tools/stanford_ner/stanford-ner-2018-10-16'
os.environ['ONLINE'] = '1'

app = Celery('fracking_tools')

# app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('fracking_tools.settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))