from django.contrib import admin
from .models import Category, Product
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Class to access the Category model via Django Admin panel
    """
    list_display = (
        'friendly_name', 'name',)
    search_fields = (
        'friendly_name', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Class to access the Products model via Django Admin panel
    """
    list_display = (
        'name', 'category',
        'for_sensory_needs',
        'sku', 'price', 'rating',)
    search_fields = (
        'category', 'name',
        'for_sensory_needs',
        'price', 'rating',)
