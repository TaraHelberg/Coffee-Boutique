from django.shortcuts import render


def contact_us(request):
    """ A view to return the conact_us page """

    return render(request, 'contact_us/contact_us.html')
