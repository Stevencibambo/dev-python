#import the necessary packages
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
]