from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Article

def index(request):
    articles = Article.get_last(9)
    return render(request, 'articles/index.html', locals())

def single_article(request, id):
    article = Article.objects.get(id=id)
    articles = Article.get_last(3)
    return render(request, 'articles/single-article.html', locals())

