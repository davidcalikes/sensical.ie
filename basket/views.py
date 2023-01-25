from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from products.models import Product


def shopping_basket(request):
    """ A view to return basket page """

    return render(request, 'basket/shopping_basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of a sensory product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    product = get_object_or_404(Product, pk=item_id)

    if item_id in list(basket.keys()):
        if basket[item_id] + quantity > 10:
            messages.error(
                request,
                "Customers are restricted to a maximum of 10 items per transaction",
            )
        else:
            basket[item_id] += quantity
            messages.success(
                request,
                f"{ basket[item_id] } \
                     { product.name }'s added to basket",
            )

    elif item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    """Update and save changes to the shopping basket"""

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('shopping_basket'))


def remove_item(request, item_id):
    """
    Adjust the quantity of the specified product to the specified
    amount

    url for this function should be <str:id> not <int:id>
    - otherwise you need to add str() method for each dict representation.
    """
    basket = request.session.get('basket', {})
    quantity = basket[item_id] - 10

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)
    request.session['basket'] = basket
    if not basket:
        return redirect(reverse('shopping_basket'))
    return redirect(reverse('shopping_basket'))
