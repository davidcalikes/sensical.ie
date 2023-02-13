from django.urls import path
from .views import AllTestimonials, AddTestimonial, UpdateTestimonial

urlpatterns = [
    path("testimonials/", AllTestimonials.as_view(), name="testimonials"),
    path("add/", AddTestimonial.as_view(), name="add_testimonial"),
    path("update/<int:pk>", UpdateTestimonial.as_view(), name="update_testimonial"),
]
