from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.user_wish_list, name='user_wishlist'),
    path('wishlist/add_to_wishlist/<int:id>',
         views.add_to_wishlist, name='add_to_wishlist'),
]
