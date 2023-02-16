from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import ContactUsForm


def contact_us(request, *args, **kwargs):
    """ A view to return the conact_us page """
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            subject = form.cleaned_data['subject'],
            message = form.cleaned_data['message'],
            form.save()

            send_mail({subject}, f'{name}, {email}, {message}',
                      settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],
                      fail_silently=False)
            messages.success(request, 'Thank you for contacting us we will reply within 24 hours!')

            return redirect(reverse('home'))
        else:
            messages.error(request, 'Something went wrong with your submission. Please try again.')

    else:
        form = ContactUsForm()

    return render(request, 'company_info/contact_us.html', {'form': form})
