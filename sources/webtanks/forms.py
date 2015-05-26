from __future__ import unicode_literals

from django import forms
from django.contrib import auth
from django.utils.translation  import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

from .users import UserModel

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		auth.login(request, user)

		return HttpResponseRedirect("/webtanks/")
	else:
		return HttpResponseRedirect("/webtanks/registration/login/")

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/webtanks/registration/logout/")

class RegistrationForm(UserCreationForm):

	required_css_class = 'required'
	email = forms.EmailField(label=_("E-mail"))

	class Meta:
		model  = UserModel()
		fields = ("username", "email")
