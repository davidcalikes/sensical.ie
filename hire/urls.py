from django.urls import path
from . import views

urlpatterns = [
    path('hire', views.hire, name='hire')
]
