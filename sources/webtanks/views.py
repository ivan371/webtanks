#!/usr/bin/python
# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .field import field
from .tank import tank
from .bot import bot
from .bullet import bullet
import threading
from webtanks import signals
from .models import RegistrationProfile
from .models import Rating
from .models import Field
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
from django.contrib.auth.models import User
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import __main__
import random
import json
import time
import threading

def index(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/webtanks/login/")
	else:
		try:
			__main__.t[__main__.numthread].append(threading.Thread(target=switchmod, args=(request)))
			__main__.t[__main__.numthread].start()
			print "NUMBER!!!", threading.activeCount()
			__main__.t[__main__.numthread].join()
		except:
			__main__.numthread = 0
			__main__.t = []
		__main__.numthread = __main__.numthread + 1
		return render(request, 'webtanks/switch_mod.html')
		
def is_in_game(request):
	t = Field.objects.all()
	for result in t:
		if(str(result.user1) == str(request.user)):
			request.session['field'] = result.field_id
			result.state = 1
			result.save()
			return 1
	return 0

@csrf_exempt
def list_users(request):
	c = {}
	c.update(csrf(request))
	if(is_in_game(request)):
		__main__.request11 = 0
		__main__.request12 = 0
		__main__.request21 = 0
		__main__.request22 = 0
		__main__.live = 1
		__main__.life = 1
		__main__.name = 0
		__main__.oldfield = field()
		__main__.oldfield.createTank(120, 690)
		__main__.oldfield.createOpp(900, 120)
		__main__.oldfield.num = 0
		return (request, 'webtanks/multitanks.html') 
	else:
		f = open("webtanks/templates/webtanks/users.html", "w")
		f.write('{% extends "base.html" %}'
			"{% load staticfiles %}"
			"{% block title %}Выбор противника{% endblock %}"
			"{% block content %}"
			'<div style="display: table; margin: 0 auto; padding: 1em 0; text-align: center;">'
			'<label for=""num""><font size="6" color="black" face="Calibri">Список пользователей и их рейтинг: </font></label>'
			"</div>")
		t = Rating.objects.order_by("-rating")
		for result in t:
			f.write('<div style="display: table; margin: 0 auto; padding: 5px; text-align: center;"><font size="5" color="navy" face="Arial">')
			f.write(str(result.who))
			f.write(" - ")
			f.write(str(result.rating))
			f.write('</font>')
			f.write('</div>')

		f.write("<form action=""/webtanks/chmod/num/users/"" method=""post"">"
			'<div style="display: table; margin: 0 auto; padding: 1em 0; text-align: center;">'
			'<label for=""num""><font size="6" color="black" face="Calibri">Введите имя противника: </font></label>'
			"<input id=""num"" type=""text"" name=""num"">"
			"<input type=""submit"" value=""OK"">"
			"</form>"
			"</div>"
			"{% endblock %}")
		f.close
		return (request, 'webtanks/users.html')

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
			request.session[str(request.user)] = 1
			(request, val) = (list_users(request))
			return render(request, val)

@csrf_exempt
def getkey(request):
	c = {}
	c.update(csrf(request))
	arr = [2, 0, 2, 0, 0, 0, 0]
	if(__main__.request11 == 1):
		arr[0] = 1
		arr[1] = __main__.request12
		arr[2] = __main__.name
		arr[3] = str(request.user)
		arr[4] = __main__.oldfield.Xtanks[0]
		arr[5] = __main__.oldfield.Ytanks[0]
		arr[6] = __main__.life
		print(__main__.newfield.Xtanks[0], __main__.newfield.Ytanks[0])
		__main__.request11 = 0
	return HttpResponse (json.dumps(arr), content_type="application/json")

@csrf_exempt
def gotkey(request):
	c = {}
	c.update(csrf(request))
	arr = [2, 0, 2, 0, 0, 0, 0]
	if(__main__.request21 == 1):
		arr[0] = 1
		arr[1] = __main__.request22
		arr[2] = __main__.name
		arr[3] = str(request.user)
		arr[4] = __main__.newfield.Xtanks[0]
		arr[5] = __main__.newfield.Ytanks[0]
		arr[6] = __main__.life
		__main__.request21 = 0
	return HttpResponse (json.dumps(arr), content_type="application/json")
	
@csrf_exempt
def tr(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		POST = request.POST
		__main__.request11 = 1
		__main__.request12 = POST['name']
		__main__.name = 0
		return __main__.oldfield.treating(request)

@csrf_exempt
def tr1(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		POST = request.POST
		__main__.request21 = 1
		__main__.request22 = POST['name']
		__main__.name = 1
		return __main__.newfield.treating(request)

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
		return render(request, 'webtanks/newtanks.html')	

@csrf_exempt
def multiwin(request):
	c = {}
	c.update(csrf(request))
	try:
		Field.objects.get(field_id = request.session['field']).delete()
	except:
		a = 0
	if request.method == 'POST':
		f = Rating.objects.get(who = User.objects.get(username=str(request.user)))
		f.rating = f.rating + 100
		f.save()
		return render(request,'webtanks/WIN.html')

@csrf_exempt
def win(request):
	c = {}
	c.update(csrf(request))
	try:
		Field.objects.get(field_id = request.session['field']).delete()
	except:
		a = 0
	if request.method == 'POST':
		f = Rating.objects.filter(who = User.objects.get(username=str(request.user)))
		for t in f:
			t.rating = t.rating + 100
			t.save()
		return render(request,'webtanks/WIN.html')

@csrf_exempt
def lose(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		return render(request,'webtanks/LOSE.html')	

@csrf_exempt
def multilose(request):
	c = {}
	c.update(csrf(request))
	try:
		Field.objects.get(field_id = request.session['field']).delete()
	except:
		a = 0
	__main__.life = 2
	if request.method == 'POST':
		return render(request,'webtanks/LOSE.html')	

@csrf_exempt
def numbot(request):
	c = {}
	c.update(csrf(request))
	POST = request.POST  
	if request.method == 'POST':
		res = __main__.res
		return HttpResponse (json.dumps(res), content_type="application/json")		

@csrf_exempt
def who(request):
	c = {}
	c.update(csrf(request))
	POST = request.POST  
	arr = [0, 0]
	if request.method == 'POST':
		if(__main__.user1 == str(request.user)):
			arr[0] = 0
		else:
			arr[0] = 1
		arr[1] = str(request.user)
		return HttpResponse (json.dumps(arr), content_type="application/json")		

@csrf_exempt
def choose(request):
	c = {}
	c.update(csrf(request))
	POST = request.POST
	res = 0
	t = Field.objects.filter(field_id = request.session['field'])
	for r in t:
		if(r.state == 1):
			res = 1
	return HttpResponse (json.dumps(res), content_type="application/json")
	
@csrf_exempt
def con(request):
	c = {}
	c.update(csrf(request))
	POST = request.POST  
	return render(request, 'webtanks/multitanks.html')

@csrf_exempt
def users(request):
	c = {}
	c.update(csrf(request))
	POST = request.POST  
	if request.method == 'POST':
		u1 = int(time.mktime(time.gmtime()))
		user = User.objects.get(username=str(POST['num']))
		us = User.objects.get(username=str(request.user))
		f = Field(field_id = u1, user1 = user, user2 = us)
		f.save()
		__main__.user1 = str(POST['num'])
		__main__.user2 = str(request.user)
		__main__.newfield = field()
		__main__.newfield.createTank(900, 120)
		__main__.newfield.createOpp(120, 690)
		__main__.newfield.num = 0
		request.session['field'] = u1
		return render(request, 'webtanks/connecting.html')

@csrf_exempt
def breakwall(request):
	c = {}
	c.update(csrf(request))	
	return __main__.newfield.breakwall(request)
	
@csrf_exempt
def gettank(request):
	c = {}
	c.update(csrf(request))	
	arr = [0, 0]
	POST = request.POST  
	if request.method == 'POST':
		arr[0] = __main__.newfield.Xtanks[0]
		arr[1] = __main__.newfield.Ytanks[0]
		return HttpResponse (json.dumps(arr), content_type="application/json")	
		
@csrf_exempt
def oppbreakwall(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		POST = request.POST
		if(__main__.user2 == str(request.user)):
			return __main__.newfield.breakwall(request)
		else:
			return __main__.oldfield.breakwall(request)
