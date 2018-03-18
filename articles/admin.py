from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    list_filter = ['author']
    # readonly_fields = ('created',)

admin.site.register(Article, ArticleAdmin)
