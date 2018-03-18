from django.contrib import admin
from .models import Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user_name', 'article_id', 'created')
    list_filter = ['article_id']
    readonly_fields = ('created',)

admin.site.register(Comment, CommentAdmin)