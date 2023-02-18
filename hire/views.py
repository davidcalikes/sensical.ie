from django.shortcuts import render


def hire(request):
    """ A view to return home/landing page """

    return render(request, 'hire/hire.html')
