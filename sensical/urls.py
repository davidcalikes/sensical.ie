from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('about/', include('about.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('hire/', include('hire.urls')),
    path('packages/', include('packages.urls')),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt", content_type="text/plain")
        ),
]


handler404 = "sensical.views.page_not_found_view"
handler500 = "sensical.views.error_view"
