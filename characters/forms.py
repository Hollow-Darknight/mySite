from django import forms

from characters.models import Commentaire


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['nom_auteur', 'texte']