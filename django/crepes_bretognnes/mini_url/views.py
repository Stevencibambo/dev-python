from django.shortcuts import redirect, get_object_or_404, render
from .models import MiniURL
from .forms import MiniURLForm

# Create your views here.
def liste(request):
    """Affichage des redirections"""
    minis = MiniURL.objects.order_by('-nb_access')
    return render(request, 'mini_url/liste.html', locals())

def nouveau(request):
    """Ajout d'une redirectiono"""
    if request.method == 'POST':
        form = MiniURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(liste)
    else:
        form = MiniURLForm()
    return render(request, 'mini_url/nouveau.html', {'form': form})
    
def redirection(request, code):
    """Redirection vers l'URL enregistree """
    mini = get_object_or_404(MiniURL, code=code)
    mini.nb_access += 1
    mini.save()

    return redirect(mini.url, permanent=True)