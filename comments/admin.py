from django.contrib import admin
from comments.models import Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'created_at', 'user', 'post']
    list_filter = ['created_at']
    search_fields = ['content']
    list_display_links = ['id', 'content']
