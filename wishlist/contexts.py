from django.shortcuts import get_object_or_404
from products.models import Product
from django.contrib.auth.models import User


def get_wishlist_status(request):

    products = Product.objects.filter(users_wishlist=request.user)

    return {"users_wishlist": products}
