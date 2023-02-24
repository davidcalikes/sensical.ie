from django.contrib import admin
from .models import Packages, CustomPackage


@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'equipment',
                    'duration', 'sensory_items_included',
                    'sensory_items_type', 'image_url',
                    'image', 'discount_voucher', 'price')
    search_fields = ('package_name', 'equipment',
                     'duration', 'sensory_items_included',
                     'sensory_items_type', 'image_url',
                     'image', 'discount_voucher', 'price')


@admin.register(CustomPackage)
class CustomPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',
                    'package_requirements')
    search_fields = ('name', 'email',
                     'package_requirements')
