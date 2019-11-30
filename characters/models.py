from django.db import models

from django.template.defaultfilters import slugify


# Create your models here.
class Personnage(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    origine = models.CharField(max_length=100)
    resumer = models.TextField(blank=True, null=True)
    histoire = models.TextField(blank=True, null=True)
    image_filename = models.CharField(max_length=255)

    def __str__(self):
        return """Nom : {}
        Prénom : {}
        Age : {}
        Origine : {}
        Résumer : {}
        Histoire : {}
        """.format(self.nom,
                   self.prenom,
                   self.age,
                   self.origine,
                   self.resumer,
                   self.histoire)

    def slug(self):
        return "{}-{}".format(self.prenom, self.nom)


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
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    status = models.CharField(max_length=20,
                              default=STATUS_VISIBLE,
                              choices=STATUS_CHOICES)
    moderation_text = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} (status={})'.format(self.author_name, self.text[:20], self.status)
