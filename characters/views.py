from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect

from myBlog import navigation
from characters.models import Personnage


# Create your views here.
def all_characters(request):
    personnages = Personnage.objects.all().order_by('-created_at')

    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_CHARACTERS),
        'personnages': personnages,
    }

    return render(request, 'characters/view_all.html', context)


def character_details(request, slug):
    prenom = slug.capitalize()
    personnage = Personnage.objects.get(prenom=prenom)

    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_CHARACTERS),
        'personnage': personnage
    }

    return render(request, 'characters/character_details.html', context)
