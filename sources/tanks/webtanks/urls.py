from django.conf.urls import url

from . import views
from .tank import tank

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^webtanks/latest\.html$', views.index),
    url(r'^treating/$', views.treating),
<<<<<<< HEAD
    #url(r'^treating/$', tank.treating),
=======
    #url(r'^treatind/$, tank.treating),
>>>>>>> ee8256552be2510bf4c8a4a6f22b0d0a97ac4425
]
