from django.shortcuts import get_object_or_404
from products.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def get_wishlist_status(request):
    products = 0
    if request.user.is_authenticated:
        products = Product.objects.filter(users_wishlist=request.user)

    return {"users_wishlist": products}
