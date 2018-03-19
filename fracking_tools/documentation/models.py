# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')

    def __str__(self):
        return 'Category: {}'.format(self.name)


class Section(models.Model):
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return 'Section: {}'.format(self.name)
