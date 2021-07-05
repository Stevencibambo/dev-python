from .models import Article, Categorie, Contact
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm, ArticleForm, NouveauContactForm

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

def contact(request):
    # construire le formulaire soit avec les donnees poste
    # soit un formulaire vide si l'utilisateur access pour la premiere fois
    form = ContactForm(request.POST or None)
    # Nous virifions que les donnees envoyes sont valides
    # cette methode renvoie false s'il n'y a pas de donnees
    # dans le formulaire ou qu'il contient des erreurs
    if form.is_valid():
        # Ici nous pouvons traiter les donnees du formulaires
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # nous pourrions ici envoyer l'e-mail grace aux donnees
        # que nous venons de recuperer
        envoi = True
    # quoiqu'il arrive, on affiche la page du formulaire
    return render(request, 'blog/contact.html', locals())

def add_article(request):
    form = ArticleForm(request.POST, instance=Article)

    if form.is_valid():
        titre = form.cleaned_data['titre']
        auteur = form.cleaned_data['auteur']
        contenu = form.cleaned_data['contenu']
        Categorie = form.cleaned_data['categorie']
        form.save()

    return render(request, 'blog/add_article.html', locals())

def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data['nom']
        contact.adresse = form.cleaned_data['adresse']
        contact.photo = form.cleaned_data['photo']
        contact.save()
        sauvegarde = True
    
    return render(request, 'blog/nouveau_contact.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })

def voir_contact(request):
    return render(
        request,
        'blog/voir_contacts.html',
        {'contacts': Contact.objects.all()}
    )