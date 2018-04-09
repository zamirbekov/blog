from django.template.context_processors import request
from articles.forms import ArticleSearchForm
from categories.models import Category

def search(request):
    search_form = ArticleSearchForm()
    categories = Category.get_all()
    return ({"search_form": search_form, "categories": categories})