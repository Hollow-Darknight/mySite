from django.shortcuts import render

from characters.models import Personnage


# Create your views here.
def all_characters(request):
    personnages = Personnage.objects.all()

    context = {
        'personnages': personnages,
    }

    return render(request, 'characters/view_all.html', context)