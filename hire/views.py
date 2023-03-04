from django.shortcuts import render


def hire(request):
    """ A view to return hire page """

    return render(request, 'hire/hire.html')
