from django.contrib import admin
from .models import Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user_name', 'created')
    list_filter = ['created']
    readonly_fields = ('created',)

admin.site.register(Comment, CommentAdmin)