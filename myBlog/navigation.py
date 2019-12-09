# Script de navigation permettant de gérer automatiquement la barre de navigation du site

from django.urls import reverse_lazy
from django.contrib import auth
from django.contrib.auth.models import User

NAV_HOME = "Accueil"
NAV_CHARACTERS = "Personnages"
# NAV_LOGIN = "Connexion"
# NAV_SIGNUP = "Inscription"
# NAV_LOGOUT = "Déconnexion"

NAV_ITEMS = (
    (NAV_HOME, reverse_lazy('index')),
    (NAV_CHARACTERS, reverse_lazy('characters-all')),
    # (NAV_LOGIN, reverse_lazy('login')),
    # (NAV_SIGNUP, reverse_lazy('signup')),
    # (NAV_LOGOUT, reverse_lazy('logout'))
)


def navigation_items(selected_item):
    items = []
    for name, url in NAV_ITEMS:
        items.append({
            'name': name,
            'url': url,
            'active': True if selected_item == name else False
        })

    return items
