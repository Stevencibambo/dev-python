from django.conf.urls import url
from django.shortcuts import redirect
from . import views

urlpatterns = [
    url(r'^$', views.liste, name='url_liste'),
    url(r'^nouveau$', views.nouveau, name='url_nouveau'),
    url(r'^(?P<code>\w{6})/$', views.redirection, name='url_redirection'),
]