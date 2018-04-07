# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from utils import configuration
from utils.event_builder import EventBuilder
from StringIO import StringIO
from documentation.models import Section
from .tasks import build_events_from_files

from docx import Document

from networktools.files.readers import FileReader
import csv

from celery.result import AsyncResult
from fracking_tools.celery import app

def index_view(request):
    context = {
        'event_networks_card': configuration.BUILD_NETWORKS_FROM_EVENTS_CARD,
        'pair_networks_card': configuration.BUILD_NETWORKS_FROM_PAIRS_CARD,
        'compare_networks': configuration.COMPARE_NETWORKS_CARD,
        'build_events': configuration.BUILD_EVENTS_FROM_FILES_CARD,
    }
    return render(request, 'network_tools/index.html', context)


def results_view(request): 
    context = {}

    if request.method == 'GET': 
        task_id = request.GET.get('task-id')  
        if task_id: 
            work = AsyncResult(task_id, app=app)
            context['task_id'] = task_id
            context['work'] = work

    return render(request, 'network_tools/results.html', context)

def build_events_view(request):
    context = {
        'section': Section.objects.filter(name='Build Events From Files')[0],
    }
    return render(request, 'network_tools/events_builder/events_builder.html', context)


def build_events_now_view(request):
    if request.method == 'POST':
        output_csv_file = request.POST.get('output-events-csv')
        files = request.FILES.getlist('input-files')

        # f = FileReader(files[0].file).read()
        # print ExtensionHandler(files[0].name).get_extension()

        # with open(files[0].file, 'rb') as f: 
        
        # reader = FileReader(files[0])

        # print reader.filename

        contents = [FileReader(f).read() for f in files]


        results = build_events_from_files.delay(contents)

        print results.get()

        # print results

        # print results
        # rows = EventBuilder(files).create_events()

        # if rows:
        #     memory_file = StringIO()
        #     csv.writer(memory_file).writerows(rows)
        #     response = HttpResponse(memory_file.getvalue().replace('nan', ''), content_type='text/csv')
        #     response['Content-Disposition'] = 'attachment; filename={}'.format(output_csv_file
        #                                                                        if output_csv_file.lower().endswith('.csv')
        #                                                                        else '{}.csv'.format(output_csv_file))
        #     return response

    return redirect('network_tools:build_events')































































def build_events_networks_view(request):
    context = {
        'section': Section.objects.filter(name='Build Networks From Events')[0],
    }
    return render(request, 'network_tools/events_networks/events_networks.html', context)


def build_pairs_networks_view(request):
    context = {
        'section': Section.objects.filter(name='Build Networks From Node Pairs')[0],
    }
    return render(request, 'network_tools/pairs_networks/pairs_networks.html', context)


def compare_networks_view(request):
    context = {
        'section': Section.objects.filter(name='Compare Networks')[0],
    }
    return render(request, 'network_tools/compare_networks/compare_networks.html', context)
