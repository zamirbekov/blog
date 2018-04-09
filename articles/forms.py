from django import forms
from django.forms import TextInput, ModelForm

from .models import Article

class ArticleSearchForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={'class': 'src-input', 'placeholder': 'Поиск',
                                          'name': 'q', 'type': 'text'})}