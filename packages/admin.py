from django.contrib import admin
from .models import Packages


@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'equipment',
                    'duration', 'sensory_items_included',
                    'sensory_items_type', 'image_url',
                    'image', 'discount_voucher',)
    search_fields = ('package_name', 'equipment',
                     'duration', 'sensory_items_included',
                     'sensory_items_type', 'image_url',
                     'image', 'discount_voucher',)
