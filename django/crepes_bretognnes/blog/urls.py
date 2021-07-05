from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('article/<id_article>', views.view_article),
    path('article/<str:tag>', views.list_article_by_tag),
    path('article/<int:year>/<int:month>', views.list_articles),
    path('contact/', views.contact, name='contact'),
    path('add_article/', views.add_article, name='add_article'),
    path('add_contact/', views.nouveau_contact, name='nouveau_contact'),
    path('voir_contact', views.voir_contact, name='voir_contacts'),
]