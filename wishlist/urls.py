from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/add_to_wishlist/<int:id>',views.add_to_wishlist, name='user_wishlist'),
]
