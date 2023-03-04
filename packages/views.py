from django.views.generic.base import TemplateView
from django.views import generic
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Packages, CustomPackage
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
    Superuser can update an existing package
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
    """
    User can request a custom package
    """
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
    return render(request,
                  'packages/package_request_form.html', {'form': form})


class PackageRequestList(LoginRequiredMixin, generic.ListView):
    """
    Displays any custom package requests to admin user.
    """
    model = CustomPackage
    template_name = 'packages/custom_packages.html'
    context_object_name = 'package_request_list'

    def get_queryset(self):
        return CustomPackage.objects.all(
        ).order_by('name')


def DeletePackageRequest(request, package_request_id):
    """Admin User can delete a Package Request """
    package_request_instance = get_object_or_404(CustomPackage,
                                                 pk=package_request_id)

    package_request_instance.delete()
    messages.success(request, 'Package request deleted!')
    return redirect(reverse('custom'))
