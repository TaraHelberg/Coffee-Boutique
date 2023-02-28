from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Blog(models.Model):
    """
    Model for the Blog Posts
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts')
    content = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='blogs/', max_length=1024,
                              null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Orders the Blogs in Descending order.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string method "AKA :The Magic method""
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Generate unique slug
        """
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
