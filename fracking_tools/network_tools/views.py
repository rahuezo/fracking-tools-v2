# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.http import JsonResponse

from utils import configuration
from documentation.models import Section

from networktools.files.readers import FileReader

from .tasks import build_events_from_files
from celery.result import AsyncResult
from fracking_tools.celery import app

import csv


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
    response = redirect('network_tools:build_events')

    if request.method == 'POST' and request.FILES and request.POST.get('output-events-csv'):
        output_csv_file = request.POST.get('output-events-csv')
        files = [(f.name, FileReader(f).read()) for f in request.FILES.getlist('input-files')]
        results = build_events_from_files.delay(files)

        response['Location'] += '?task={}&csv={}'.format(results, output_csv_file)
    return response


def check_task_status(request): 
    task_id = request.GET.get('task-id')
    task = AsyncResult(task_id, app=app)    
    return JsonResponse({'status': task.status})


def download_events_file_view(request): 
    if request.method == 'GET' and request.GET.get('task') and request.GET.get('csv'):         
        task_id = request.GET.get('task')
        output_csv = request.GET.get('csv')
        
        task = AsyncResult(task_id, app=app)
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename="{}.csv"'.format(output_csv)
        
        writer = csv.writer(response)

        for row in task.get(): 
            writer.writerow(row)
        return response
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
