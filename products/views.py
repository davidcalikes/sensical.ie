from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """ A view to return all products to the products page """

    products = Product.objects.all()
    query = ""

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Please type what you are looking for...")
                return redirect(
                    reverse('products'))

    queries = Q(name__icontains=query) | Q(description__icontains=query)
    products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return an individual product detail page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
