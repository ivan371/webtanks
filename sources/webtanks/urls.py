from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.views.generic.base import TemplateView

from django.contrib.auth import views as auth_views

from . import views
from .auth_views import RegistrationView
from .auth_views import ActivationView

from .tank import tank

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^webtanks/latest\.html$', views.index),
	url(r'^chmod/num/treating/$', views.treating),
	url(r'^chmod/num/flight/$', views.flight),
	url(r'^chmod/num/treating/users/$', views.treating),
	url(r'^chmod/num/flight/users/$', views.flight),
	url(r'^chmod/num/shot/users/$', views.shot),
	url(r'^chmod/num/bot/$', views.bot),
	url(r'^chmod/num/numbot/$', views.numbot),
	url(r'^chmod/num/$', views.numbots),
	url(r'^chmod/num/win/$', views.win),
	url(r'^chmod/num/multiwin/$', views.multiwin),
	url(r'^chmod/num/lose/$', views.lose),
	url(r'^chmod/num/multilose/$', views.multilose),
	url(r'^chmod/num/shot/$', views.shot),
	url(r'^chmod/num/users/$', views.users),
	url(r'^chmod/$', views.switchmod),
	url(r'^chmod/num/users/choose/$', views.choose),
	url(r'^chmod/con/$', views.con),
	url(r'^chmod/con/tr1/$', views.tr1), #us1
	url(r'^chmod/tr1/$', views.tr), #us2
	url(r'^chmod/con/who/$', views.who),
	url(r'^chmod/who/$', views.who),
	url(r'^chmod/con/isend/$', views.isend),
	url(r'^chmod/isend/$', views.isend),
	url(r'^chmod/con/tr2/$', views.tr2),
	url(r'^chmod/tr2/$', views.tr2), 
	url(r'^chmod/con/fl/$', views.fl),
	url(r'^chmod/fl/$', views.fl),
	url(r'^chmod/con/getkey/$', views.getkey), #us1
	url(r'^chmod/getkey/$', views.gotkey), #us2
	url(r'^chmod/con/breakwall/$', views.oppbreakwall),
	url(r'^chmod/num/gettank/$', views.gettank),
	url(r'^chmod/breakwall/$', views.oppbreakwall),
	url(r'^chmod/num/breakwall/$', views.breakwall),
	url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='auth_login'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='auth_logout'),
	url(r'^password/change/$', auth_views.password_change, {'post_change_redirect': reverse_lazy('auth_password_change_done')}, name='auth_password_change'),
	url(r'^password/change/done/$', auth_views.password_change_done, name='auth_password_change_done'),
	url(r'^password/reset/$', auth_views.password_reset, {'post_reset_redirect': reverse_lazy('auth_password_reset_done')}, name='auth_password_reset'),
	url(r'^password/reset/complete/$', auth_views.password_reset_complete, name='auth_password_reset_complete'),
	url(r'^password/reset/done/$', auth_views.password_reset_done, name='auth_password_reset_done'),
	url(r'^activate/complete/$', TemplateView.as_view(template_name='registration/activation_complete.html'), name='registration_activation_complete'),
	url(r'^activate/(?P<activation_key>\w+)/$', ActivationView.as_view(), name='registration_activate'),
	url(r'^register/complete/$', TemplateView.as_view(template_name='registration/registration_complete.html'), name='registration_complete'),
	url(r'^register/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'), name='registration_disallowed'),
	#url(r'^treatind/$, tank.treating),
]

from django import get_version
from distutils.version import LooseVersion
if (LooseVersion(get_version()) >= LooseVersion('1.6')):
	urlpatterns += patterns('', url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, {'post_reset_redirect': reverse_lazy('auth_password_reset_complete')}, name='auth_password_reset_confirm'))
else:
	urlpatterns += patterns('', url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'post_reset_redirect': reverse_lazy('auth_password_reset_complete')}, name='auth_password_reset_confirm'))

if getattr(settings, 'INCLUDE_REGISTER_URL', True):
	urlpatterns += patterns('', 
		url(r'^register/$',
			RegistrationView.as_view(),
			name='registration_register'),
	)
