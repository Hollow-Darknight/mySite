from django.shortcuts import render, get_object_or_404

from characters.models import Personnage


def landpage(request):
    return render(request, 'index.html')


def homepage():
    return None