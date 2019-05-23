# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.http import JsonResponse

from utils import configuration
from documentation.models import Section

from celery.result import AsyncResult
from fracking_tools.celery import app

import csv, io, zipfile


from utils import configuration
from .tasks import compare_documents, tag_documents_keywords, tag_documents_ner, compute_document_statistics


def index_view(request): 
    context = {
        'compare_documents': configuration.COMPARE_DOCS_CARD, 
        'tag_documents_kwds': configuration.TAG_DOCS_KEYWORDS_CARD,
        'tag_documents_ner': configuration.TAG_DOCS_NER_CARD,
        'doc_stats': configuration.DOC_STATS_CARD
    }
    return render(request, 'document_tools/index.html', context)


# Compare documents

def compare_documents_view(request): 
    context = {
        'section': Section.objects.filter(name='Compare Documents')[0],
    }
    return render(request, 'document_tools/compare_documents/compare_documents.html', context)


def compare_documents_now_view(request):
    response = redirect('document_tools:compare_documents')

    if request.method == 'POST' and request.FILES and request.POST.get('output-csv'):
        output_csv_file = request.POST.get('output-csv')
        files = request.FILES.getlist('input-files')
        # results = compare_documents.delay(files)
        results = compare_documents(files)

        print "Results: ", results

        response['Location'] += '?task={}&csv={}'.format(results, output_csv_file)
    return response


def download_document_comparisons_view(request): 
    if request.method == 'GET' and request.GET.get('task') and request.GET.get('csv'):         
        task_id = request.GET.get('task')
        output_csv = request.GET.get('csv')
        
        task = AsyncResult(task_id, app=app)
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename="{}.csv"'.format(output_csv)
        
        writer = csv.writer(response)
        writer.writerow(['File A', 'File B', 'Cosine Similarity', 'Jaccard Similarity'])

        for row in task.get(): 
            writer.writerow(row)
        return response
    return redirect('document_tools:compare_documents')

# End Compare documents


# Tag Documents for Keywords

def tag_documents_keywords_view(request): 
    context = {
        'section': Section.objects.filter(name='Tag Documents for Keywords')[0],
    }
    return render(request, 'document_tools/tag_documents_keywords/tag_documents.html', context)


def tag_documents_keywords_now_view(request):
    response = redirect('document_tools:tag_documents_keywords')

    if request.method == 'POST' and request.FILES and request.POST.get('output-zip') and request.POST.get('keywords-list'):
        output_zip_file = request.POST.get('output-zip')
        files = request.FILES.getlist('input-files')
        keywords = [kw.strip() for kw in request.POST.get('keywords-list').split(',')]

        results = tag_documents_keywords.delay(files, keywords)

        response['Location'] += '?task={}&zip={}'.format(results, output_zip_file)
    return response

# End Tag documents for keywords


# Tag Documents Using NER

def tag_documents_ner_view(request): 
    context = {
        'section': Section.objects.filter(name='Tag Documents Using Stanford\'s Named Entity Recognizer (NER)')[0],
    }
    return render(request, 'document_tools/tag_documents_ner/tag_documents.html', context)


def tag_documents_ner_now_view(request):
    response = redirect('document_tools:tag_documents_ner')

    if request.method == 'POST' and request.FILES and request.POST.get('output-zip'):
        output_zip_file = request.POST.get('output-zip')
        files = request.FILES.getlist('input-files')

        results = tag_documents_ner.delay(files)

        response['Location'] += '?task={}&zip={}'.format(results, output_zip_file)
    return response

# End Tag documents using NER


# Compute Document Statistics

def compute_document_statistics_view(request): 
    context = {
        'section': Section.objects.filter(name='Compute Document Statistics')[0]
    }
    return render(request, 'document_tools/document_statistics/document_statistics.html', context)


def compute_document_statistics_now_view(request):
    response = redirect('document_tools:compute_document_statistics')

    if request.method == 'POST' and request.FILES and request.POST.get('output-csv') and request.POST.get('keywords-list'):
        output_csv_file = request.POST.get('output-csv')
        files = request.FILES.getlist('input-files')
        keywords = [kw.strip() for kw in request.POST.get('keywords-list').split(',')]

        results = compute_document_statistics.delay(files, keywords)

        response['Location'] += '?task={}&csv={}'.format(results, output_csv_file)
    return response


def download_document_analysis_view(request): 
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
    return redirect('document_tools:compute_document_statistics')

# End Compute document statistics 



# Download tagged documents 

def download_tagged_documents_view(request): 
    if request.method == 'GET' and request.GET.get('task') and request.GET.get('zip'):         
        task_id = request.GET.get('task')
        output_zip = request.GET.get('zip')
        
        task = AsyncResult(task_id, app=app)

        zip_io = io.BytesIO()

        # fill zip file 
        with zipfile.ZipFile(zip_io, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file: 
            # Create csv io here 

            for fname, content in task.get(): 
                zip_file.writestr(fname, content)
                
        # response will be zip file 
        response = HttpResponse(zip_io.getvalue(), content_type='application/x-zip-compressed')
        response['Content-Disposition'] = 'attachment;filename="{}.zip"'.format(output_zip)
        response['Content-Length'] = zip_io.tell()

        print "Current task ID: ", task_id
        print "Output Zip: ", output_zip
        return response
    return redirect('document_tools:index')


def check_task_status(request): 
    task_id = request.GET.get('task-id')
    task = AsyncResult(task_id, app=app)    
    
    return JsonResponse({'status': task.status, 'traceback': task.traceback })