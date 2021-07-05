from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=10)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'article'
        ordering = ['date']

    def __str__(self):
        return  self.titre

class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom
    
class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to='photo/')

    def __str__(self):
        return self.nom