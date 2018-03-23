from django.http import HttpResponseRedirect

from .forms import CommentForm
from articles.models import Article

def add_comment(request, article_id):
    form = CommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.article = Article.objects.get(id=article_id)
        form.save()
        return HttpResponseRedirect('/article/%s/' % article_id)
