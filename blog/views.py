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


def blog_detail(request, slug):
    """
    View Full Blog Post
    """
    context = {}
    blog = Blog.objects.get(slug=slug)

    context['blog'] = blog

    template = 'blog/blog_detail.html'
    context = {
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, slug):
    """
    View Add a Blog Post
    """
    blog = Blog.objects.get(slug=slug)
    user = request.user

    if request.method == "POST":
        form = BlogForm(request.POST or None,
                        request.FILES or None, instance=blog)
        if user == blog.author:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                blog = obj
                messages.success(request, "Successfully Edited your Blog Post")
                return redirect(reverse('blog_detail', args=[obj.slug]))
            else:
                messages.error(request, "Failed to Update Blog Post.")
        else:
            messages.info(request, 'You are not allowed to do that as you are \
                not the Blog Author!')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are Editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'blog': blog,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, slug):
    """
    View Delete a Blog Post
    """
    blog = Blog.objects.get(slug=slug)
    user = request.user
    if blog.author == user:
        blog.delete()
        messages.success(request, f'You have deleted {blog.title}')
        return redirect(reverse('blog'))
    else:
        messages.error(request, "Unable to Delete Blog.")

    template = 'blog/delete_blog.html'
    context = {
        'blog': blog,
    }

    return render(request, template, context)
