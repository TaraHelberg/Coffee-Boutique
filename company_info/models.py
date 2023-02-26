from django.db import models
from django.utils import timezone


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
