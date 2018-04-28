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
        'compare_documents': configuration.COMPARE_DOCS_CARD,
        'tag_documents_kwds': configuration.TAG_DOCS_KEYWORDS_CARD,
        'tag_documents_ner': configuration.TAG_DOCS_NER_CARD,
        'doc_stats': configuration.DOC_STATS_CARD
    }
    return render(request, 'fthome/index.html', context)
