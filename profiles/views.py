from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    """ Display the user's profile. """

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
