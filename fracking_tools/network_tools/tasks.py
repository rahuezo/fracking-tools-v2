# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from networktools.events.builder import EventBuilder


@shared_task
def build_events_from_files(files):
    builder = EventBuilder(files)
    return builder.build() 


@shared_task
def build_event_networks(files): 
    return 


@shared_task
def build_pair_networks(files): 
    return 
