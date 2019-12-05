from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect

from myBlog import navigation
from characters.models import Personnage, Commentaire
from characters.forms import CreateCommentForm


# Create your views here.
def all_characters(request):
    personnages = Personnage.objects.all().order_by('-created_at')

    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_CHARACTERS),
        'personnages': personnages,
    }

    return render(request, 'characters/view_all.html', context)


def character_details(request, slug, message=""):
    prenom = slug.capitalize()
    personnage = get_object_or_404(Personnage, prenom=prenom)

    comments = personnage.commentaires.exclude(status=Commentaire.STATUS_HIDDEN).order_by('created_at')

    if request.method == 'POST':
        comment_form = CreateCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.personnage = personnage
            comment.save()

            args = [personnage.slug, 'Votre commentaire a été envoyé !']
            return HttpResponseRedirect(reverse('character-details-message', args=args) + '#commentaires')
    else:
        comment_form = CreateCommentForm()

    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_CHARACTERS),
        'personnage': personnage,
        'comments': comments,
        'comment_form': comment_form,
        'message': message
    }

    return render(request, 'characters/character_details.html', context)
