from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import Blog
from .forms import BlogForm


def blog(request):
    """
    View all Blog Posts
    """
    blogs = Blog.objects.all()
    template = 'blog/blog.html'
    context = {
        'blogs': blogs
    }
    return render(request, template, context)


@login_required
def add_blog(request):
    """
    View Add a Blog Post
    """
    if request.method == "POST":
        form = BlogForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            author = request.user
            obj.author = author
            obj.save()

            messages.success(request, "Successfully added your Blog post")
            return redirect(reverse('blog_detail', args=[obj.slug]))
        else:
            messages.error(
                request, "Failed to add Blog post, please check the form is \
                    valid")
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
