from django.contrib import admin
from .models import Category, Product


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
        'name', 'category', 'description', 'in_stock',
        'for_sensory_needs', 'image', 'image_url',
        'sku', 'price', 'rating',)
    search_fields = (
        'category', 'name',
        'for_sensory_needs',
        'price', 'rating',)
