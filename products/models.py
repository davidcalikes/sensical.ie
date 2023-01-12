from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Model for product categories
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SubCategory(models.Model):
    """
    Model for product categories
    """

    class Meta:
        verbose_name_plural = 'Sub-categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model for products
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sub_category = models.ForeignKey(
        'SubCategory',
        null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    in_stock = models.BooleanField(
        default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    image = CloudinaryField(
        "Product Image", default='placeholder')

    def __str__(self):
        return self.name