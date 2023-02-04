from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse
from products.models import Product

from products.models import Product
from django.contrib.auth.models import User


# def add_to_wishlist(request):
#     """ A view to return wishlist page """

#     return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        print("product removed from wishlist")
    else:
        product.users_wishlist.add(request.user)
        print("product added to wishlist")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
