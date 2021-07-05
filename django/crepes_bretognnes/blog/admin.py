from django.contrib import admin
from .models import Article, Categorie

# Register your models here.
class ArticlAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date')
    list_filter = ('auteur', 'categorie',)
    date_hierarchy  = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'contenu')

admin.site.register(Article, ArticlAdmin)
admin.site.register(Categorie)