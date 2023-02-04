from django.db import models

from django.contrib.auth.models import User
from products.models import Product


class wishlist(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
