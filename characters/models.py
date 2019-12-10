from django.db import models

from django.template.defaultfilters import slugify


# Create your models here.
class Personnage(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    age = models.IntegerField()
    origine = models.CharField(max_length=100)
    resumer = models.TextField(blank=True, null=True)
    histoire = models.TextField(blank=True, null=True)
    image_filename = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    publier = models.BooleanField(default=True)

    def slug(self):
        return slugify(self.prenom)

    def __str__(self):
        return self.prenom


class Galerie(models.Model):
    personnage = models.ForeignKey('Personnage',
                                   on_delete=models.CASCADE,
                                   related_name="galeries")
    images_filename = models.CharField(max_length=255)


class Commentaire(models.Model):
    STATUS_VISIBLE = "visible"
    STATUS_HIDDEN = "cacher"
    STATUS_MODERATE = "moderer"

    STATUS_CHOICES = (
        (STATUS_VISIBLE, "Visible"),
        (STATUS_HIDDEN, "Cacher"),
        (STATUS_MODERATE, "Modérer")
    )

    personnage = models.ForeignKey('Personnage',
                             on_delete=models.CASCADE,
                             related_name='commentaires')
    nom_auteur = models.CharField(max_length=100)
    texte = models.TextField()
    status = models.CharField(max_length=20,
                              default=STATUS_VISIBLE,
                              choices=STATUS_CHOICES)
    texte_moderation = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} (status={})'.format(self.nom_auteur, self.texte[:20], self.status)
