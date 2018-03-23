#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

from articles.models import Article

class Comment(models.Model):
    created = models.DateTimeField(verbose_name=('Дата создания'), auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name=('Статья'))
    user_name = models.CharField(max_length=120, verbose_name=('Имя комментатора'))
    email = models.EmailField(verbose_name=('Почта'))
    text = models.TextField(verbose_name=('Текст комментария'))

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created']
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'