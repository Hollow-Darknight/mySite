from django.contrib import admin
from django.db import models
from django.forms import Textarea

from characters.models import Personnage, Galerie, Commentaire


@admin.register(Personnage)
class PersonnageAdmin(admin.ModelAdmin):
    search_fields = ['prenom', 'nom']
    list_display = (
        'prenom',
        'nom',
        'image_filename',
        'publier',
        'created_at'
    )

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 90})},
    }


@admin.register(Galerie)
class GalerieAdmin(admin.ModelAdmin):
    search_fields = ['personnage__nom', 'personnage__prenom', 'image_filename']


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    search_fields = ['personnage__nom', 'personnage__prenom', 'author_name']
    list_display = (
        'personnage',
        'author_name',
        'status',
        'moderation_text',
        'text'
    )

    list_editable = ('status', 'moderation_text')
    list_filter = ('status', )

