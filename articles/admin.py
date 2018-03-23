from django.contrib import admin

from .models import Article
from comments.models import Comment

class ArticleInline(admin.StackedInline):
    model = Comment
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    list_filter = ['author']
    inlines = [ArticleInline]

admin.site.register(Article, ArticleAdmin)
