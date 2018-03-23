from django.shortcuts import render

from .models import Article
from comments.models import Comment
from comments.forms import CommentForm

def index(request):
    articles = Article.get_last(9)
    return render(request, 'articles/index.html', locals())

def single_article(request, id):
    article = Article.objects.select_related('author').get(id=id)
    articles = Article.get_last(3)
    comment_form = CommentForm
    comments = Comment.objects.filter(article = id)
    return render(request, 'articles/single-article.html', locals())
