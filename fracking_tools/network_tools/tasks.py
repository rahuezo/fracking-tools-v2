# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from networktools.events.builder import EventBuilder


@shared_task
def build_events_from_files(files): 
    builder = EventBuilder(files)
    return builder.build()