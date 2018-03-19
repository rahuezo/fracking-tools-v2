# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index_view(request):
    return render(request, 'network_tools/index.html')


def build_events_networks_view(request):
    return render(request, 'network_tools/events_networks/events_networks.html')


def build_pairs_networks_view(request):
    return render(request, 'network_tools/pairs_networks/pairs_networks.html')


def compare_networks_view(request):
    return render(request, 'network_tools/compare_networks/compare_networks.html')
