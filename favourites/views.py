from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from products.models import Product
from .models import Favourites


def favourites(request):
    """Favourite Products View"""
    return render(request, 'favourites/favourites.html')
