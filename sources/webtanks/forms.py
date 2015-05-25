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
    return HttpResponseRedirect("/webtanks/registration/logout")

class RegistrationForm(UserCreationForm):

    required_css_class = 'required'
    email = forms.EmailField(label=_("E-mail"))
    
    class Meta:
        model  = UserModel()
        fields = ("username", "email")


class RegistrationFormTermsOfService(RegistrationForm):

    tos = forms.BooleanField(widget=forms.CheckboxInput,
                             label=_('I have read and agree to the Terms of Service'),
                             error_messages={'required': _("You must agree to the terms to register")})


class RegistrationFormUniqueEmail(RegistrationForm):

    def clean_email(self):

        if UserModel().objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']


class RegistrationFormNoFreeEmail(RegistrationForm):

    bad_domains = ['aim.com', 'aol.com', 'email.com', 'gmail.com',
                   'googlemail.com', 'hotmail.com', 'hushmail.com',
                   'msn.com', 'mail.ru', 'mailinator.com', 'live.com',
                   'yahoo.com']

    def clean_email(self):

        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain in self.bad_domains:
            raise forms.ValidationError(_("Registration using free email addresses is prohibited. Please supply a different email address."))
        return self.cleaned_data['email']
