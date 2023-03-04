from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm
import cloudinary.uploader
from django.contrib.auth.decorators import user_passes_test


def all_products(request):
    """ A view that displays all products."""

    products = Product.objects.all()
    available_items = Product.objects.all().values('in_stock')
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Please type what you are looking for...")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(
                queries)

    current_sorting = f'{sort}_{direction}'
    available_items = Product.objects.filter(in_stock=True)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'available_items': available_items,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return an individual product detail page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@user_passes_test(lambda u: u.is_superuser)
def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_data = cloudinary.uploader.upload(image)['secure_url']

            product = form.save(commit=False)
            product.image = image_data
            product.image_url = image_data
            product.save()

            messages.success(request, 'Successfully added product!',)
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                """
                Failed to add product.
                Please ensure the form is valid.
                """)
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@user_passes_test(lambda u: u.is_superuser)
def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            if 'image' in request.FILES:
                image = form.cleaned_data['image']
                image_data = cloudinary.uploader.upload(
                    image)['secure_url']
            else:
                image_data = product.image

            product = form.save(commit=False)
            product.image = image_data
            product.save()

            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Please submit valid form.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    basket = request.session.get('basket', {})
    if basket:
        messages.error(request, """There are items in you basket!
                                Please remove all basket items before
                                editing the product inventory.""")
    else:
        product.delete()
        messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
