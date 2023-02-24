from django.views.generic.base import TemplateView, View
from django.views import generic
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Packages
from .forms import PackageForm, CustomPackageForm


class CurrentPackages(TemplateView):
    """A view that reders all available hire packages"""

    template_name = "packages/packages.html"

    def get_context_data(self, **kwargs):
        packages = Packages.objects.all()
        all_packages_list = []
        for package in packages:
            all_packages_list.append(package)

        context = super().get_context_data(**kwargs)
        context["packages"] = packages
        context["all_packages_list"] = all_packages_list
        return context


class AddPackage(SuccessMessageMixin, generic.CreateView):
    """
    Superuser can add a package
    """
    model = Packages
    form_class = PackageForm
    template_name = 'packages/packages_form.html'
    success_url = reverse_lazy('packages')
    success_message = "Package added successfully!"

    def form_valid(self, form):
        """
        Auto applies foreign key and auto generated settings.
        """
        form.instance.created_by = self.request.user
        return super(AddPackage, self).form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.add_message(self.request, messages.ERROR,
                             "Invalid form input... See errors below")
        return self.render_to_response(self.get_context_data(form=form))


class UpdatePackage(SuccessMessageMixin, generic.edit.UpdateView):
    """
    Superuser can update enrolled an existing package
    """
    model = Packages
    form_class = PackageForm
    template_name = 'packages/packages_form.html'
    success_url = reverse_lazy('packages')
    success_message = "Package updated successfully!"

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.add_message(self.request, messages.ERROR,
                             "Invalid form input... See errors below")
        return self.render_to_response(self.get_context_data(form=form))


class DeletePackage(SuccessMessageMixin, generic.DeleteView):
    """
    Superuser can delete an existing package
    """
    model = Packages
    form_class = PackageForm
    success_url = reverse_lazy('packages')
    success_message = "Package deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePackage, self).delete(request, *args, **kwargs)


def PackageRequest(request):
    if request.method == 'POST':
        form = CustomPackageForm(request.POST)
        if form.is_valid():
            custom_package = form.save(commit=False)
            if request.user.is_authenticated:
                custom_package.email = request.user.email
            custom_package.save()
            return render(request, 'packages/package_request_success.html')
    else:
        if request.user.is_authenticated:
            form = CustomPackageForm(initial={'email': request.user.email})
        else:
            form = CustomPackageForm()
    return render(request, 'packages/package_request_form.html', {'form': form})
