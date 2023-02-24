from django import forms

from .models import Packages, CustomPackage


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
                  'image', 'discount_voucher', 'price')


class CustomPackageForm(forms.ModelForm):
    class Meta:
        model = CustomPackage
        fields = ['name', 'email', 'package_requirements']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
