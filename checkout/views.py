from django.shortcuts import render

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request,
                       "There's nothing in your Shopping Cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MKKiRGofEiIqbhZzo7YP5McVElxCTJvyETWoTznvKkHUDhUcR7HcHIxDcEOSMY4QNmQJS7On2rOtRMV3GeS7Zg500fE0ehDfE',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
