from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .field import field
from .tank import tank
from .bot import bot
from .bullet import bullet

from webtanks import signals
from .models import RegistrationProfile
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

def index(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/webtanks/login/")
	else:
		return render(request, 'webtanks/switch_mod.html')


@csrf_exempt
def sessions(request):
	c = {}
	c.update(csrf(request))
	#if 1:	
	if request.session[str(request.user)]  != 2:
		f = open("webtanks/templates/webtanks/users.html", "w")
		f.write("{% load staticfiles %}"
			"<html>"
			"<body>")
		dic = request.session.keys()
		arr = []	
		print(dic)
		for i in dic:
			tmp = str(i)
			print(str(i))
			if request.session[tmp] == 1:
				f.write("<H1>")
				f.write(tmp)
				f.write("</H1>")
		f.write("<form action=""/webtanks/users/"" method=""post"">"
			"<label for=""num"">input users_name: </label>"
			"<input id=""num"" type=""text"" name=""num"">"
			"<input type=""submit"" value=""OK"">"
			"</form>"
			"</body>"
			"</html>")
		f.close
		return (request, 'webtanks/users.html')
	else:
		return (request, 'webtanks/multitanks.html')

@csrf_exempt
def switchmod(request):
	c = {}
	c.update(csrf(request))
	POST = request.POST  
	if request.method == 'POST':
		res = int(POST['num'])
		if res == 1:
			return render(request, 'webtanks/params.html')
		else:
			print(request.session[str(request.user)])
			request.session[str(request.user)] = 1
			(request, val) = (sessions(request))
			return render(request, val)


@csrf_exempt
def treating(request):
	c = {}
	c.update(csrf(request))
	__main__.newfield.num = 0
	return __main__.newfield.treating(request)

@csrf_exempt
def flight(request):
	c = {}
	c.update(csrf(request))
	return __main__.newfield.flight(request)

@csrf_exempt
def bot(request):
	c = {}
	c.update(csrf(request))
	return __main__.newfield.bott(request)

@csrf_exempt
def shot(request):
	c = {}
	c.update(csrf(request))
	return __main__.newfield.shot(request)	

@csrf_exempt
def numbots(request):
	c = {}
	c.update(csrf(request))
	POST = request.POST  
	if request.method == 'POST':
		res = int(POST['num'])
		__main__.newfield = field()
		__main__.newfield.createTank(120, 690)
		__main__.res = res
		#for i in range (res):
		#	__main__.newfield.createBot(random.randint(100, 1000), random.randint(100, 700))
		return render(request, 'webtanks/newtanks.html')

@csrf_exempt
def win(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':	
		return redirect('webtanks/templates/	webtanks/WIN.html')

@csrf_exempt
def lose(request):
	c = {}
	c.update(csrf(request))
	res = 1	
	if request.method == 'POST':
		return redirect('webtanks/templates/webtanks/LOSE.html')	

@csrf_exempt
def numbot(request):
	c = {}
	c.update(csrf(request))
	POST = request.POST  
	if request.method == 'POST':
		res = __main__.res
		return HttpResponse (json.dumps(res), content_type="application/json")		
