from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_basket, name='shopping_basket')
]
