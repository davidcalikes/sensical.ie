from django.views.generic.base import TemplateView
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import clientTestimonial
from .forms import testimonialForm
import cloudinary.uploader


class AllTestimonials(TemplateView):
    """A view that reders all client testimonials"""

    template_name = "testimonials/testimonials.html"

    def get_context_data(self, **kwargs):
        testimonials = clientTestimonial.objects.all()
        all_testimonials_list = []
        for testimonial in testimonials:
            all_testimonials_list.append(testimonial)

        context = super().get_context_data(**kwargs)
        context["testimonials"] = testimonials
        context["all_testimonials_list"] = all_testimonials_list

        return context


class AddTestimonial(SuccessMessageMixin, generic.CreateView):
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

        image = self.request.FILES.get('image')

        if image:
            result = cloudinary.uploader.upload(image)
            image_url = result.get('url')
        else:
            image_url = clientTestimonial.photo_url.field.default

        form.instance.photo_url = image_url

        return super().form_valid(form)


class UpdateTestimonial(SuccessMessageMixin, generic.edit.UpdateView):
    """
    Superuser can update an existing testimonial
    """
    model = clientTestimonial
    form_class = testimonialForm
    template_name = 'testimonials/testimonial_form.html'
    success_url = reverse_lazy('testimonials')
    success_message = "Testimonial updated successfully!"

    def form_valid(self, form):
        image = self.request.FILES.get('image')

        if image:
            result = cloudinary.uploader.upload(image)
            image_url = result.get('url')

            self.object.photo_url = image_url

        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.add_message(self.request, messages.ERROR,
                             "Invalid form input... See errors below")
        return self.render_to_response(self.get_context_data(form=form))


class DeleteTestimonial(SuccessMessageMixin, generic.DeleteView):
    """
    Superuser can delete an existing testimonial
    """
    model = clientTestimonial
    form_class = testimonialForm
    success_url = reverse_lazy('testimonials')
    success_message = "Testimonial deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteTestimonial, self).delete(request, *args, **kwargs)
