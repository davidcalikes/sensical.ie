from .models import clientTestimonial


def get_testimonials(request):
    return {"all_testimonials_list": clientTestimonial.objects.all()}
