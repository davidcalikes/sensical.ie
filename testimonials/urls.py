from django.urls import path
from .views import AllTestimonials, AddTestimonial

urlpatterns = [
    path("testimonials/", AllTestimonials.as_view(), name="testimonials"),
    path("testimonials/", AddTestimonial.as_view(), name="add_testimonial"),
]
