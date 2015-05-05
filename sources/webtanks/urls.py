from django.conf.urls import url

from . import views
from .tank import tank

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^webtanks/latest\.html$', views.index),
    url(r'^treating/$', views.treating),
    #url(r'^treating/$', tank.treating),
    #url(r'^treatind/$, tank.treating),
]
