from django.contrib import admin
from .models import ContactUs, Blog
from django_summernote.admin import SummernoteModelAdmin


class BlogAdmin(SummernoteModelAdmin):
    """Allows admin to manage Blog via the admin panel"""
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


class ContactUsAdmin(admin.ModelAdmin):
    """Allows admin to manage enquiries via the admin panel"""
    list_display = (
        'name',
        'email',
        'subject',
        'message',
        'date_submitted',
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
