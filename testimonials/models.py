from django.db import models
from cloudinary.models import CloudinaryField


class clientTestimonial(models.Model):
    """
    Model class for the testimonials app
    """
    name = models.CharField(max_length=256)
    testimonial = models.TextField(blank=True, null=True)
    photo_url = models.URLField(
        max_length=1024, blank=True, null=True,
        default='https://res.cloudinary.com/djck2eqxo/'
                'image/upload/v1677845806/'
                'placeholder_testimonial_u1gzwo.webp')
    image = CloudinaryField(
        "Testimonial Image", default='placeholder')

    def __str__(self):
        return self.name
