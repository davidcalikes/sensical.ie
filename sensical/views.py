from django.shortcuts import render


def page_not_found_view(request, exception):
    """ 404 Page Not Found """
    return render(request, "404.html")


def error_view(request):
    """ 500 Internal Server Error """
    return render(request, "500.html")
