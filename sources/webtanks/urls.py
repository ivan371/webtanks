from django.conf.urls import url
from . import views
from .tank import tank

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^webtanks/latest\.html$', views.index),
	url(r'^num/treating/$', views.treating),
	url(r'^num/flight/$', views.flight),
	url(r'^num/bot/$', views.bot),
	url(r'^num/numbot/$', views.numbot),
	url(r'^num/$', views.numbots),
	#url(r'^treatind/$, tank.treating),
]
