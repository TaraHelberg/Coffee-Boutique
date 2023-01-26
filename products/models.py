from django.db import models


class Category(models.Model):
    """
    Model for the Category
    Used from Boutique Ado
    Credit to Code Institute
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model for the Product
    Used & Modified slightly from Boutique Ado
    Credit to Code Institute
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True, blank=True)
    update_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
