from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Review


def reviews(request):
    """ Renders Reviews Page """
    review_list = (
        Review.objects.all().order_by("-created_on")
    )
    return render(
        request, 'reviews/reviews.html', {"reviews_list": review_list})
