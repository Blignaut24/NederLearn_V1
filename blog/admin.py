from django.contrib import admin
from .models import Blogpost, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Blogpost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('blog_title', 'slug', 'status', 'created_on')
    search_fields = ('blog_title', 'content')
    prepopulated_fields = {'slug': ('blog_title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('user', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user', 'body', 'post')
    actions = ['approved_comments']

    def approved_comments(self, request, queryset):
        queryset.update(approved=True)
