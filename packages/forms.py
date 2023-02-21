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
                  'duration', 'peripherals_included',
                  'peripherals_type', 'image_url',
                  'image', 'discount_voucher',)
