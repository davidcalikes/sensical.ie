from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product


def shopping_basket(request):
    """ A view to return basket page """

    return render(request, 'basket/shopping_basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of a sensory product to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if quantity > 10:
        quantity = 10

    elif quantity < 1:
        quantity = 1

    elif item_id in list(basket.keys()):
        if basket[item_id] + quantity > 10:
            messages.error(
                request,
                """
                Customers are restricted to a
                maximum of 10 items per transaction
                """,
            )
        else:
            basket[item_id] += quantity
            messages.success(
                request,
                f"{ basket[item_id] } \
                     { product.name }'s added to basket",
            )
    else:
        basket[item_id] = quantity
        messages.success(
                request,
                f"{ basket[item_id] } \
                     { product.name }'s added to basket",
            )

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    """Update and save changes to the shopping basket"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 10:
        quantity = 10
    elif quantity < 1:
        quantity = 1

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
                request,
                f"There are now { basket[item_id] } \
                     { product.name }'s in your basket",
        )
    else:
        basket.pop(item_id)
        messages.success(
                request,
                f"Could not add { basket[item_id] } \
                     { product.name }'s to your basket",
        )

    request.session['basket'] = basket
    return redirect(reverse('shopping_basket'))


def remove_item(request, item_id):
    """
    Remove entire quantity of a given product.
    """
    product = get_object_or_404(Product, pk=item_id)
    basket = request.session.get('basket', {})
    quantity = basket[item_id] - 10

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)
        messages.success(
                request,
                f"All { product.name }'s removed from your basket",
        )
    request.session['basket'] = basket
    if not basket:
        return redirect(reverse('shopping_basket'))
    return redirect(reverse('shopping_basket'))
