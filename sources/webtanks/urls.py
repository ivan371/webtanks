from django.conf.urls import url
from . import views
from .tank import tank

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^webtanks/latest\.html$', views.index),
	url(r'^chmod/num/treating/$', views.treating),
	url(r'^chmod/num/flight/$', views.flight),
	url(r'^chmod/num/bot/$', views.bot),
	url(r'^chmod/num/numbot/$', views.numbot),
	url(r'^chmod/num/$', views.numbots),
	url(r'^chmod/num/win/$', views.win),
	url(r'^chmod/num/lose/$', views.lose),
	url(r'^chmod/num/shot/$', views.shot),
	url(r'^chmod/$', views.switchmod)
	#url(r'^treatind/$, tank.treating),
]
