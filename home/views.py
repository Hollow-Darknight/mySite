from django.shortcuts import render, get_object_or_404

from characters.models import Personnage
from myBlog import navigation


def landpage(request):
    return render(request, 'index.html')


def homepage(request):
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_HOME),
    }
    return render(request, 'home/accueil.html', context)