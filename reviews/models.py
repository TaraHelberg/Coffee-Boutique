from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Review(models.Model):
    """Product Review Model"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=250, blank=True)
    rate = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Orders the comments in Ascending order.
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.review} by {self.user}"
