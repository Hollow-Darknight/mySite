from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from myBlog import navigation
from characters.models import Personnage, Commentaire
from characters.forms import CreateCommentForm, EditCommentForm


# Create your views here.
def all_characters(request):
    personnages = Personnage.objects.filter(publier=True).order_by('-created_at')

    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_CHARACTERS),
        'personnages': personnages,
    }

    return render(request, 'characters/view_all.html', context)


def character_details(request, slug, message=''):
    prenom = slug.capitalize()
    personnage = get_object_or_404(Personnage, prenom=prenom)

    comments_list = personnage.commentaires.exclude(status=Commentaire.STATUS_HIDDEN).order_by('-created_at')

    # Paginator pour n'afficher que 10 commentaires à la fois
    page = request.GET.get('page', 1)

    paginator = Paginator(comments_list, 10)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        comment_form = CreateCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.personnage = personnage
            comment.save()

            args = [slug, "post-comment"]
            return redirect(reverse('character-details-message', args=args) + '#commentaires')
    else:
        comment_form = CreateCommentForm()

    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_CHARACTERS),
        'personnage': personnage,
        'comments': comments,
        'comments_list': comments_list,
        'comment_form': comment_form,
        'message': message,
    }

    return render(request, 'characters/character_details.html', context)