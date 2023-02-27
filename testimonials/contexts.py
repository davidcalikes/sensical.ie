from .models import clientTestimonial


def get_testimonials(request):

    testimonials = clientTestimonial.objects.all()

    return {"testimonials": testimonials}
