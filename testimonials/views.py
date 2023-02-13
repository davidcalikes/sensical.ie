from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import clientTestimonial
from .forms import testimonialForm


class AllTestimonials(TemplateView):
    """A view that reders all client testimonials"""

    template_name = "testimonials.html"

    def get_context_data(self, **kwargs):
        testimonials = clientTestimonial.objects.all()

        context = super().get_context_data(**kwargs)
        context["testimonials"] = testimonials

        return context


class AddTestimonial(TemplateView):
    """A superuser can add a client testimonial"""

    template_name = "add_testimonial.html"

    def post(self, request, *args, **kwargs):

        form = testimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Testimonial was successfully added!"
            )
            return redirect(reverse("testimonials"))
        else:
            
            messages.error(
                request,
                "Invalid form input!",
            )
            context = {"form": form}

            return render(request, self.template_name, context)

    def test_func(self):
        return not self.request.user.is_superuser
