#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

from categories.models import Category
from authors.models import Author

class Article(models.Model):
    created = models.DateTimeField(verbose_name=('Дата создания'), auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=('Автор'))
    title = models.CharField(max_length=120, verbose_name=('Название статьи'))
    photo = models.ImageField(verbose_name=('Изображение'), upload_to='images/articles')
    text = models.TextField(verbose_name=('Текст'))
    category = models.ManyToManyField(Category, related_name='article', verbose_name=('Категория'))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'

    @classmethod
    def get_last(cls, length):
        articles = cls.objects.select_related().order_by('-created')[:length]
        return articles


