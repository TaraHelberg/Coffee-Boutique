from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog


class BlogAdmin(SummernoteModelAdmin):
    """Allows admin to manage Blog via the admin panel"""
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


admin.site.register(Blog, BlogAdmin)
