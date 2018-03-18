#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=120, verbose_name=('Имя'))
    photo = models.ImageField(verbose_name=('Изображение'), upload_to='images/authors')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name = u'Автор'
        verbose_name_plural = u'Авторы'