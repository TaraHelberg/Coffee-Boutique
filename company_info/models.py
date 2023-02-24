from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Blog(models.Model):
    """
    Model for the Blog
    """
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    """
    Contact Us Form Model.
    """
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
    date_submitted = models.DateTimeField(default=timezone.now)

    class Meta:

        ordering = ['-date_submitted']
