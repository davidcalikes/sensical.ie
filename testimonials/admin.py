from django.contrib import admin
from .models import clientTestimonial


@admin.register(clientTestimonial)
class clientTestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'testimonial',
                    'photo_url', 'image')
    search_fields = ('name', 'testimonial',
                     'photo_url', 'image')
