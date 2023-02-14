from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Favourites(models.Model):
    """Shopper Favourites Products model"""

    class Meta:
        """Removes extra 's' from Model name"""
        verbose_name_plural = 'Favourites'

    product = models.ManyToManyField(Product, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return object string"""
        return f"{self.user}'s Favourites"
