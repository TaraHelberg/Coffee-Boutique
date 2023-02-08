from django.shortcuts import render
from .models import Review


def reviews(request):
    """ A view that renders the Reviews contents page """

    return render(request, 'reviews/reviews.html')
