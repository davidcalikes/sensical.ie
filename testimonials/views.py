from django.views.generic.base import TemplateView
from django.views import generic
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.urls import reverse_lazy

from .models import clientTestimonial
from .forms import testimonialForm


class AllTestimonials(TemplateView):
    """A view that reders all client testimonials"""

    template_name = "testimonials/testimonials.html"

    def get_context_data(self, **kwargs):
        testimonials = clientTestimonial.objects.all()

        context = super().get_context_data(**kwargs)
        context["testimonials"] = testimonials

        return context


class AddTestimonial(generic.CreateView):
    """
    Superuser can add a testimonial
    """
    model = clientTestimonial
    form_class = testimonialForm
    template_name = 'testimonials/testimonial_form.html'
    success_url = reverse_lazy('testimonials')
    success_message = "Testimonial added successfully!"

    def form_valid(self, form):
        """
        Auto applies foreign key and auto generated settings.
        """
        form.instance.created_by = self.request.user
        return super(AddTestimonial, self).form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.add_message(self.request, messages.ERROR,
                             "Invalid form input... See errors below")
        return self.render_to_response(self.get_context_data(form=form))


class UpdateTestimonial(generic.edit.UpdateView):
    """
    Superuser can update enrolled an existing testimonial
    """
    model = clientTestimonial
    form_class = testimonialForm
    template_name = 'testimonials/testimonial_form.html'
    success_url = reverse_lazy('testimonials')
    success_message = "Testimonial updated successfully!"

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.add_message(self.request, messages.ERROR,
                             "Invalid form input... See errors below")
        return self.render_to_response(self.get_context_data(form=form))


class DeleteTestimonial(generic.DeleteView):
    """
    Superuser can delete an existing testimonial
    """
    model = clientTestimonial
    form_class = testimonialForm
    template_name = 'testimonials/testimonial_form.html'
    success_url = reverse_lazy('testimonials')
    success_message = "Testimonial deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteTestimonial, self).delete(request, *args, **kwargs)
