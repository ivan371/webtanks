from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^webtanks/latest\.html$', views.index),
    url(r'^treating/$', views.treating),
]
