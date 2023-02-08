from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """Review Admin Class"""
    list_display = (
        'user',
        'product',
        'review',
        'rate',
        'created_on',
        'updated_on',
    )

    ordering = ('-created_on',)
