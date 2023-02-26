from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import BlogForm


def blog(request):
    """View Blog Posts"""

    return render(request, 'blog/blog.html')


def add_blog(request):
    """Add Blog"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST or None)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added Blog Post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request,
                           f'Failed to add blog.'
                           f'Please ensure the form is valid.'
                           )
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
