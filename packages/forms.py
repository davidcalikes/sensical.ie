from django import forms

from .models import Packages


class PackageForm(forms.ModelForm):
    """
    Form to add/edit hire package.
    """
    class Meta:
        """
        Form has all required fields from Packages model
        """
        model = Packages
        fields = ('package_name', 'equipment',
                  'duration', 'sensory_items_included',
                  'sensory_items_type', 'image_url',
                  'image', 'discount_voucher',)
