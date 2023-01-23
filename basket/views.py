from django.shortcuts import render


def shopping_basket(request):
    """ A view to return basket page """

    return render(request, 'basket/shopping_basket.html')

