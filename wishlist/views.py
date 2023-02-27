from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from products.models import Product


def user_wish_list(request):
    """ A view to return wishlist page """

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        messages.success(request, 'Removed from wishlist!')
    else:
        product.users_wishlist.add(request.user)
        messages.success(request, 'Added to wishlist!')

    return HttpResponseRedirect(request.META["HTTP_REFERER"],)
