from django import forms

from .models import clientTestimonial


class testimonialForm(forms.ModelForm):
    """
    Form to add/edit client testimonial.
    """
    class Meta:
        """
        Form has all required fields from clientTestimonial model
        """
        model = clientTestimonial
        fields = ('name', 'testimonial',
                  'image')
