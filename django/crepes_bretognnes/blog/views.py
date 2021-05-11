from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    """Exemple de page no valide au niveau HTML pour que l'example soit conciss"""
    return HttpResponse("""
    <h1>Bienvenue sur mon blog !</h1><p>Les crepes bretonnes ca tue mouettes en plein vol !</p>
    """)

def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifient (ou ID, ici un numero)
    Son ID est le second  parametre de la fonction (pour rappel, le premier)
    parametre est toujours la requete de l'utilisateur
    """
    return HttpResponse(
        "Vous avez demande l'article n*{0}!".format(id_article)
    )

def list_articles(request, month, year):
    """liste des articles d'un mois precis."""
    return HttpResponse(
        "Vous avez demande les articles de {0} {1}".format(month, year)
    )

def list_article_by_tag(request):
    """"""
    return HttpResponse("")
