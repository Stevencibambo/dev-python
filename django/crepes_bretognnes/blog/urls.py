from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('article/<id_article>', views.view_article),
    path('article/<str:tag>', views.list_article_by_tag),
    path('article/<int:year>/<int:month>', views.list_articles),
]