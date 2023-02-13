from django.contrib import admin
from .models import Favourites


class FavouritesAdmin(admin.ModelAdmin):
    """
    Favourites Admin.
    """
    list_display = ('user',)


admin.site.register(Favourites, FavouritesAdmin)
