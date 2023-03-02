from django.shortcuts import render
from products.models import Product


def index(request):
    """
    Index / Home page
    Return View with carousel 4 Products Recently Added
    """
    products = Product.objects.filter().order_by('-created_on')[:4]
    template = 'home/index.html'
    context = {
        'products': products
    }

    return render(request, template, context)
