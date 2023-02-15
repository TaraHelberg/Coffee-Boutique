from django.shortcuts import render

# Create your views here.


def favourites(request):
    """ A view to return the index page """

    return render(request, 'favourites/favourites.html')
