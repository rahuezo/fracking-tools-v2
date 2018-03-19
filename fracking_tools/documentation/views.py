# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Category, Section
from django.contrib import messages


def index_view(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'documentation/index.html', context)


def edit_view(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'documentation/edit/edit.html', context)


def add_category_view(request):
    if request.method == 'POST':
        category_name = request.POST.get('new-category-name').title()
        category_description = request.POST.get('new-category-description')

        if Category.objects.filter(name=category_name).count() == 0:
            Category.objects.create(name=category_name, description=category_description)
            messages.success(request, 'Added category <strong>{}</strong>.'.format(category_name),
                             extra_tags='added')
        else:
            messages.error(request, 'Category <strong>{}</strong> already exists!'.format(category_name), extra_tags='exists')

    return redirect('documentation:edit')


def add_section_view(request):
    if request.method == 'POST':
        section_category = request.POST.get('section-category')
        section_name = request.POST.get('section-name').title()
        section_body = request.POST.get('section-body')

        selected_category = Category.objects.get(pk=section_category)

        if Section.objects.filter(name=section_name, category=selected_category).count() == 0:
            Section.objects.create(category=selected_category, name=section_name, body=section_body)

            messages.success(request, 'Added section <strong>{}</strong>.'.format(section_name), extra_tags='added')
        else:
            messages.error(request, 'Section <strong>{}</strong> already exists!'.format(section_name), extra_tags='exists')
    return redirect('documentation:edit')



