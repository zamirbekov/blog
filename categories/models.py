#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=120, verbose_name=('Название'))
    photo = models.ImageField(verbose_name=('Изображение'), upload_to='images/categories')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    @classmethod
    def get_all(cls):
        categories = cls.objects.select_related().order_by('title')
        return categories
