from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .field import field
from .tank import tank
from .bot import bot
from .bullet import bullet

from webtanks import signals
from .models import RegistrationProfile
from .models import Rating
from .users import UserModel

from django.shortcuts import redirect
from django.views.generic.base import TemplateView
try:
	from django.utils.module_loading import import_string
except ImportError:
	from .utils import import_string

#from .bot import bot
from django.conf import settings
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.contrib import auth
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import __main__
import random
import json

class _RequestPassingFormView(FormView):

	def get(self, request, *args, **kwargs):
		# Pass request to get_form_class and get_form for per-request
		# form control.
		form_class = self.get_form_class(request)
		form = self.get_form(form_class)
		return self.render_to_response(self.get_context_data(form=form))

	def post(self, request, *args, **kwargs):
		# Pass request to get_form_class and get_form for per-request
		# form control.
		form_class = self.get_form_class(request)
		form = self.get_form(form_class)
		if form.is_valid():
			# Pass request to form_valid.
			return self.form_valid(request, form)
		else:
			return self.form_invalid(form)

	def get_form_class(self, request=None):
		return super(_RequestPassingFormView, self).get_form_class()

	def get_form_kwargs(self, request=None, form_class=None):
		return super(_RequestPassingFormView, self).get_form_kwargs()

	def get_initial(self, request=None):
		return super(_RequestPassingFormView, self).get_initial()

	def get_success_url(self, request=None, user=None):
		# We need to be able to use the request and the new user when
		# constructing success_url.
		return super(_RequestPassingFormView, self).get_success_url()

	def form_valid(self, form, request=None):
		return super(_RequestPassingFormView, self).form_valid(form)

	def form_invalid(self, form, request=None):
		return super(_RequestPassingFormView, self).form_invalid(form)

from .forms import RegistrationForm

class RegistrationView(_RequestPassingFormView):

	disallowed_url = 'registration_disallowed'
	form_class = RegistrationForm
	http_method_names = ['get', 'post', 'head', 'options', 'trace']
	template_name = 'registration/registration_form.html'
	SEND_ACTIVATION_EMAIL = getattr(settings, 'SEND_ACTIVATION_EMAIL', True)
	success_url = 'registration_complete'

	def dispatch(self, request, *args, **kwargs):
		if not self.registration_allowed(request):
			return redirect(self.disallowed_url)
		return super(RegistrationView, self).dispatch(request, *args, **kwargs)

	def form_valid(self, request, form):
		new_user = self.register(request, form)
		success_url = self.get_success_url(request, new_user)

		# success_url may be a simple string, or a tuple providing the
		# full argument set for redirect(). Attempting to unpack it
		# tells us which one it is.
		try:
			to, args, kwargs = success_url
			return redirect(to, *args, **kwargs)
		except ValueError:
			return redirect(success_url)

	def register(self, request, form):
		if Site._meta.installed:
			site = Site.objects.get_current()
		else:
			site = RequestSite(request)

		if hasattr(form, 'save'):
			new_user_instance = form.save()
		else:
			new_user_instance = UserModel().objects.create_user(**form.cleaned_data)

		new_user = RegistrationProfile.objects.create_inactive_user(
			new_user=new_user_instance,
			site=site,
			send_email=self.SEND_ACTIVATION_EMAIL,
			request=request,
		)
		signals.user_registered.send(sender=self.__class__, user=new_user, request=request)
		us = Rating(who = new_user, rating = 0)
		us.save()
		return new_user

	def registration_allowed(self, request):
		return getattr(settings, 'REGISTRATION_OPEN', True)


class ActivationView(TemplateView):
	http_method_names = ['get']
	template_name = 'registration/activate.html'

	def get(self, request, *args, **kwargs):
		activated_user = self.activate(request, *args, **kwargs)
		if activated_user:
			success_url = self.get_success_url(request, activated_user)
			try:
				to, args, kwargs = success_url
				return redirect(to, *args, **kwargs)
			except ValueError:
				return redirect(success_url)
		return super(ActivationView, self).get(request, *args, **kwargs)

	def activate(self, request, activation_key):
		activated_user = RegistrationProfile.objects.activate_user(activation_key)
		if activated_user:
			signals.user_activated.send(sender=self.__class__, user=activated_user, request=request)
		return activated_user

	def get_success_url(self, request, user):
		return ('registration_activation_complete', (), {})
