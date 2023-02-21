from django.db import models
from cloudinary.models import CloudinaryField


class Packages(models.Model):
    """
    Model class for the packages app
    """
    package_name = models.CharField(max_length=256)
    equipment = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    sensory_items_included = models.BooleanField(
        default=False, null=True, blank=True)
    sensory_items_type = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    image = CloudinaryField(
        "Package Image", default='placeholder')
    discount_voucher = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name