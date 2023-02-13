from django.shortcuts import get_object_or_404
from .models import clientTestimonial


def get_testimonials(request):

    testimonials = clientTestimonial.objects.all()

    return {"testimonials": testimonials}
