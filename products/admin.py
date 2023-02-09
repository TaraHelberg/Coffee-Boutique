from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    """
    Product Admin Class
    Used & Modified slightly from Boutique Ado
    Credit to Code Institute
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Category Admin Class
    Used from Boutique Ado
    Credit to Code Institute
    """
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """Review Admin"""
    list_display = (
        'product',
        'user',
        'review',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
