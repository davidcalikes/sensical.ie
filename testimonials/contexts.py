from .models import clientTestimonial


def get_testimonials(request):
    """
    Allows site wide access to testimonials data
    """
    return {"all_testimonials_list": clientTestimonial.objects.all()}
