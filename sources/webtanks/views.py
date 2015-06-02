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
from .views_db import views_db
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
		__main__.newview = views_db()
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

@csrf_exempt
def list_users(request):
	c = {}
	c.update(csrf(request))
	if(__main__.newview.is_in_game(request)):
		__main__.request11 = 0
		__main__.request12 = 0
		__main__.request21 = 0
		__main__.request22 = 0
		__main__.live = 1
		__main__.life = 1
		__main__.name = 0
		__main__.oldfield = field()
		__main__.oldfield.createTank(120, 690)
		__main__.oldfield.num = 0
		return (request, 'webtanks/multitanks.html') 
	else:
		__main__.newview.create_users()
		return (request, 'webtanks/users.html')

def rat(request):
	__main__.newview.create_rating(request)	
	return (request, 'webtanks/rating.html')

@csrf_exempt
def switchmod(request):
	c = {}
	c.update(csrf(request))
	POST = request.POST  
	if request.method == 'POST':
		res = int(POST['num'])
		if res == 1:
			return render(request, 'webtanks/params.html')
		elif res == 2:
			(request, val) = rat(request)
			return render(request, val)
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
	return __main__.newview.change_rating(request)
	
@csrf_exempt
def win(request):
	c = {}
	c.update(csrf(request))
	return __main__.newview.change_rating(request)
	
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
	__main__.newview.delete()
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
	return __main__.newview.chooose(request)
	
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
	if str(POST['num']) == str(request.user):
		return render(request, 'webtanks/error.html')
	u1 = int(time.mktime(time.gmtime()))
	user = User.objects.get(username=str(POST['num']))
	us = User.objects.get(username=str(request.user))
	f = Field(field_id = u1, user1 = user, user2 = us)
	f.save()
	request.session['field'] = u1
	__main__.user1 = str(POST['num'])
	__main__.user2 = str(request.user)
	__main__.newfield = field()
	__main__.newfield.createTank(900, 120)
	__main__.newfield.num = 0
	request.session['field'] = u1
	return render(request, 'webtanks/connecting.html')

@csrf_exempt
def breakwall(request):
	c = {}
	c.update(csrf(request))	
	return __main__.newfield.breakwall(request)
		
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
			
@csrf_exempt
def gettank1(request):
	c = {}
	c.update(csrf(request))	
	arr = [0, 0]
	POST = request.POST  
	if request.method == 'POST':
		arr[0] = __main__.newfield.Xtanks[0]
		arr[1] = __main__.newfield.Ytanks[0]
		return HttpResponse (json.dumps(arr), content_type="application/json")	
			
@csrf_exempt
def gettank(request):
	c = {}
	c.update(csrf(request))	
	arr = [0, 0, 0, 0]
	POST = request.POST  
	if request.method == 'POST':
		arr[0] = __main__.newfield.Xtanks[0]
		arr[1] = __main__.newfield.Ytanks[0]
		arr[2] = __main__.oldfield.Xtanks[0]
		arr[3] = __main__.oldfield.Ytanks[0]
		return HttpResponse (json.dumps(arr), content_type="application/json")	
		
@csrf_exempt
def gottank(request):
	c = {}
	c.update(csrf(request))	
	arr = [0, 0, 0, 0]
	POST = request.POST  
	if request.method == 'POST':
		arr[0] = __main__.oldfield.Xtanks[0]
		arr[1] = __main__.oldfield.Ytanks[0]
		arr[2] = __main__.newfield.Xtanks[0]
		arr[3] = __main__.newfield.Ytanks[0]
		return HttpResponse (json.dumps(arr), content_type="application/json")
