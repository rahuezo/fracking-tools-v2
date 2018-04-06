# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from networktools.events.builder import EventBuilder


@shared_task
def build_events_from_files(list_of_content):
    contents = []

    for content in list_of_content: 
        contents.append(len(content))
    return contents 
    
    # builder = EventBuilder(files)
    # return builder.build()