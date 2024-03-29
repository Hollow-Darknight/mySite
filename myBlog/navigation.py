# Script de navigation permettant de gérer automatiquement la barre de navigation du site

from django.urls import reverse_lazy


NAV_HOME = "Accueil"
NAV_CHARACTERS = "Personnages"

NAV_ITEMS = (
    (NAV_HOME, reverse_lazy('home')),
    (NAV_CHARACTERS, reverse_lazy('characters-all'))
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
