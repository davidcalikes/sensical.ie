from products.models import Product


def get_wishlist_status(request):
    """
    Allows site wide access to wishlist data
    """

    products = 0
    if request.user.is_authenticated:
        products = Product.objects.filter(users_wishlist=request.user)

    return {"users_wishlist": products}
