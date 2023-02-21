from django.urls import path
from .views import CurrentPackages, AddPackage, UpdatePackage, DeletePackage

urlpatterns = [
    path("packages/", CurrentPackages.as_view(), name="packages"),
    path("add/", AddPackage.as_view(), name="add_package"),
    path("update/<int:pk>", UpdatePackage.as_view(), name="update_package"),
    path("delete/<int:pk>", DeletePackage.as_view(), name="delete_package"),
]