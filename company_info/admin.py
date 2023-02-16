from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    """Allows admin to manage enquiries via the admin panel"""
    list_display = (
        'name',
        'email',
        'subject',
        'message',
        'date_submitted',
    )


admin.site.register(ContactUs, ContactUsAdmin)
