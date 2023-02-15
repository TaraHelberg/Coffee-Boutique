from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Favourites(models.Model):
    """Shopper Favourites Products model"""

    class Meta:
        """Removes extra 's' from Model name"""
        verbose_name_plural = 'Favourites'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Return object string"""
        return f"{self.user}'s Favourites"
