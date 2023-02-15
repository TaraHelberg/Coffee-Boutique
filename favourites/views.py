from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from products.models import Product
from profiles.models import UserProfile


def favourites(request, product_id):
    """
    Add/Remove a Favourite Product
    """
    product = get_object_or_404(Product, pk=product_id)

    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)

    return redirect(reverse('product_detail', args=[product.id]))


def favourite_list(request):
    """
    Favourite product List
    """
    user = request.user
    favourite_products = user.favourites.all()

    context = {
        'is_favourite': favourite_products
    }

    return render(request, 'favourites/favourites.html', context)
