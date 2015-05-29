from __future__ import unicode_literals

import datetime
import hashlib
import random
import re

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template import RequestContext, TemplateDoesNotExist
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils import six

from django.contrib.auth.models import User
from .users import UserModel, UserModelString


try:
	from django.utils.timezone import now as datetime_now
except ImportError:
	datetime_now = datetime.datetime.now


SHA1_RE = re.compile('^[a-f0-9]{40}$')


class RegistrationManager(models.Manager):

	def activate_user(self, activation_key):

		if SHA1_RE.search(activation_key):
			try:
				profile = self.get(activation_key=activation_key)
			except self.model.DoesNotExist:
				return False
			if not profile.activation_key_expired():
				user = profile.user
				user.is_active = True
				user.save()
				profile.activation_key = self.model.ACTIVATED
				profile.save()
				return user
		return False

	def create_inactive_user(self, site, new_user=None, send_email=True, request=None, **user_info):

		if new_user == None:
			password = user_info.pop('password')
			new_user = UserModel()(**user_info)
			new_user.set_password( password )
		new_user.is_active = False
		new_user.save()

		registration_profile = self.create_profile(new_user)

		if send_email:
			registration_profile.send_activation_email(site, request)

		return new_user

	def create_profile(self, user):

		salt = hashlib.sha1(six.text_type(random.random()).encode('ascii')).hexdigest()[:5]
		salt = salt.encode('ascii')
		user_pk = str(user.pk)
		if isinstance(user_pk, six.text_type):
			user_pk = user_pk.encode('utf-8')
		activation_key = hashlib.sha1(salt+user_pk).hexdigest()
		return self.create(user=user, activation_key=activation_key)

	def delete_expired_users(self):

		for profile in self.all():
			try:
				if profile.activation_key_expired():
					user = profile.user
					if not user.is_active:
						user.delete()
						profile.delete()
			except UserModel().DoesNotExist:
				profile.delete()


@python_2_unicode_compatible
class RegistrationProfile(models.Model):
	ACTIVATED = "ALREADY_ACTIVATED"

	user = models.OneToOneField(UserModelString(), verbose_name=_('user'))
	activation_key = models.CharField(_('activation key'), max_length=40)

	objects = RegistrationManager()

	class Meta:
		verbose_name = _('registration profile')
		verbose_name_plural = _('registration profiles')

	def __str__(self):
		return "Registration information for %s" % self.user

	def activation_key_expired(self):
		expiration_date = datetime.timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
		return (self.activation_key == self.ACTIVATED or (self.user.date_joined + expiration_date <= datetime_now()))
	activation_key_expired.boolean = True

	def send_activation_email(self, site, request=None):

		ctx_dict = {}
		if request is not None:
			ctx_dict = RequestContext(request, ctx_dict)
		ctx_dict.update({
			'user': self.user,
			'activation_key': self.activation_key,
			'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
			'site': site,
		})
		subject = getattr(settings, 'REGISTRATION_EMAIL_SUBJECT_PREFIX', '') + \
				render_to_string('registration/activation_email_subject.txt', ctx_dict)
		subject = ''.join(subject.splitlines())

		message_txt = render_to_string('registration/activation_email.txt', ctx_dict)
		email_message = EmailMultiAlternatives(subject, message_txt, settings.DEFAULT_FROM_EMAIL, [self.user.email])

		try:
			message_html = render_to_string('registration/activation_email.html', ctx_dict)
		except TemplateDoesNotExist:
			message_html = None

		if message_html:
			email_message.attach_alternative(message_html, 'text/html')

		email_message.send()

class Rating(models.Model):
	who = models.ForeignKey(User)
	rating = models.IntegerField(default=0)
	
class Field(models.Model):
	field_id = models.IntegerField(unique=True)
	request11 = models.IntegerField(default = 0)
	request12 = models.IntegerField(default = 0)
	request13 = models.IntegerField(default = 0)
	request21 = models.IntegerField(default = 0)
	request22 = models.IntegerField(default = 0)
	request23 = models.IntegerField(default = 0)
	state = models.IntegerField(default = 0)
	user1 = models.ForeignKey(User, blank=True, null=True)
	user2 = models.ForeignKey(User, blank=True, null=True, related_name = 'second')
