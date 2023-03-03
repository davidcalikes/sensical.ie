from django import forms
from .models import Packages, CustomPackage
import textwrap


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
                  'sensory_items_type',
                  'image', 'discount_voucher', 'price')


class CustomPackageForm(forms.ModelForm):
    class Meta:
        model = CustomPackage
        fields = ['name', 'email', 'package_requirements']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your name'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })

        self.fields['package_requirements'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': textwrap.dedent('''\
                Enter your package requirements here, length of session,
                sensory needs, size of room etc...
                ''')
        })
