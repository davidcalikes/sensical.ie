from django.shortcuts import render


def about(request):
    """ A view to return about page """

    return render(request, 'about/about.html')
