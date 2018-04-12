# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.http import JsonResponse

from utils import configuration
from documentation.models import Section

from networktools.files.readers import FileReader

from .tasks import build_events_from_files, build_event_networks, build_pairs_networks, compare_networks
from celery.result import AsyncResult
from fracking_tools.celery import app

import csv, io, zipfile


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


# Events builder parts 

def build_events_view(request):
    context = {
        'section': Section.objects.filter(name='Build Events From Files')[0],
    }
    return render(request, 'network_tools/events_builder/events_builder.html', context)


def build_events_now_view(request):
    response = redirect('network_tools:build_events')

    if request.method == 'POST' and request.FILES and request.POST.get('output-events-csv'):
        output_csv_file = request.POST.get('output-events-csv')
        files = request.FILES.getlist('input-files')
        results = build_events_from_files.delay(files)

        response['Location'] += '?task={}&csv={}'.format(results, output_csv_file)
    return response


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

# End events builder parts 

# Events networks parts

def build_events_networks_view(request):
    context = {
        'section': Section.objects.filter(name='Build Networks From Events')[0],
    }
    return render(request, 'network_tools/events_networks/events_networks.html', context)


def build_events_networks_now_view(request):
    response = redirect('network_tools:build_enets')

    if request.method == 'POST' and request.FILES and request.POST.get('output-zip'):
        output_zip = request.POST.get('output-zip')
        header_state = True if request.POST.get('header-state') else False

        

        files = request.FILES.getlist('input-files')
        results = build_event_networks.delay(files, header_state)

        response['Location'] += '?task={}&zip={}'.format(results, output_zip)
    return response

# End events networks parts 


# Pairs networks parts 

def build_pairs_networks_view(request):
    context = {
        'section': Section.objects.filter(name='Build Networks From Node Pairs')[0],
    }
    return render(request, 'network_tools/pairs_networks/pairs_networks.html', context)


def build_pairs_networks_now_view(request):
    response = redirect('network_tools:build_pnets')

    if request.method == 'POST' and request.FILES and request.POST.get('output-zip'):
        output_zip = request.POST.get('output-zip')
        header_state = True if request.POST.get('header-state') else False

        files = request.FILES.getlist('input-files')
        results = build_pairs_networks.delay(files, header_state)

        response['Location'] += '?task={}&zip={}'.format(results, output_zip)
    return response

# End pairs networks parts 


# Download networks

def download_networks_view(request): 
    if request.method == 'GET' and request.GET.get('task') and request.GET.get('zip'):         
        task_id = request.GET.get('task')
        output_zip = request.GET.get('zip')
        
        task = AsyncResult(task_id, app=app)

        zip_io = io.BytesIO()

        # fill zip file 
        with zipfile.ZipFile(zip_io, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file: 
            # Create csv io here 

            for fname, matrix in task.get(): 
                csv_io = io.BytesIO()
                matrix.to_csv(csv_io, sep=str(u',').encode('utf-8'), index=False)
                zip_file.writestr(fname, csv_io.getvalue())
                
        # response will be zip file 
        response = HttpResponse(zip_io.getvalue(), content_type='application/x-zip-compressed')
        response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(output_zip)
        response['Content-Length'] = zip_io.tell()
    
        return response
    return redirect('network_tools:index')

# End download networks


# Compare networks parts

def compare_networks_view(request):
    context = {
        'section': Section.objects.filter(name='Compare Networks')[0],
    }
    return render(request, 'network_tools/compare_networks/compare_networks.html', context)


def compare_networks_now_view(request):
    response = redirect('network_tools:compare_nets')

    if request.method == 'POST' and request.FILES and request.POST.get('output-zip'):
        networksA_label = request.POST.get('networkA-label')
        networksA_files = request.FILES.getlist('networkA-files')

        networksB_label = request.POST.get('networkB-label')
        networksB_files = request.FILES.getlist('networkB-files')

        output_zip = request.POST.get('output-zip')

        files = (networksA_files, networksB_files)

        results = compare_networks.delay(files, networksA_label, networksB_label)

        response['Location'] += '?task={}&zip={}'.format(results, output_zip)
    return response


def download_network_comparisons_view(request): 
    if request.method == 'GET' and request.GET.get('task') and request.GET.get('zip'):         
        task_id = request.GET.get('task')
        output_zip = request.GET.get('zip')
        
        task = AsyncResult(task_id, app=app)

        zip_io = io.BytesIO()

        # fill zip file 
        with zipfile.ZipFile(zip_io, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file: 
            # Create csv io here 

            for fname, rows in task.get(): 
                csv_io = io.BytesIO()
                
                writer = csv.writer(csv_io)
                writer.writerows(rows)

                zip_file.writestr(fname, csv_io.getvalue())
                
        # response will be zip file 
        response = HttpResponse(zip_io.getvalue(), content_type='application/x-zip-compressed')
        response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(output_zip)
        response['Content-Length'] = zip_io.tell()

        return response
    return redirect('network_tools:index')


# End compare networks 


def check_task_status(request): 
    task_id = request.GET.get('task-id')
    task = AsyncResult(task_id, app=app)    
    return JsonResponse({'status': task.status})
