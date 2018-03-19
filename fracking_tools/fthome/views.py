# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from utils import configuration


def index_view(request):

    context = {
        'event_networks_card': configuration.BUILD_NETWORKS_FROM_EVENTS_CARD,
        'pair_networks_card': configuration.BUILD_NETWORKS_FROM_PAIRS_CARD,
        'compare_networks': configuration.COMPARE_NETWORKS_CARD,
        'build_events': configuration.BUILD_EVENTS_FROM_FILES_CARD,
    }
    return render(request, 'fthome/index.html', context)
