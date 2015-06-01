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
			__main__.t[__main__.numthread].join()
		except:
			__main__.numthread = 0
			__main__.t = []
			#__main__.t[__main__.numthread].append(threading.Thread(target=switchmod, args=(request)))
			#__main__.t[__main__.numthread].start()
			#	__main__.t[__main__.numthread].join()
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
		__main__.oldfield = field()
		__main__.oldfield.createTank(120, 690)
		__main__.oldfield.createOpp(120, 120)
		__main__.oldfield.num = 0
		#__main__.user1 = "1"
		#__main__.user2 = "1"
		return (request, 'webtanks/multitanks.html') 
	else:
		f = open("webtanks/templates/webtanks/users.html", "w")
		f.write("{% load staticfiles %}"
			"<html>"
			"<body>")
		t = Rating.objects.all()
		for result in t:
			f.write("<H1>")
			f.write(str(result.who))
			f.write(" ")
			f.write(str(result.rating))
			f.write("</H1>")

		f.write("<form action=""/webtanks/chmod/num/users/"" method=""post"">"
			"<label for=""num"">input users_name: </label>"
			"<input id=""num"" type=""text"" name=""num"">"
			"<input type=""submit"" value=""OK"">"
			"</form>"
			"</body>"
			"</html>")
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
			#t1 = threading.Thread(target=tr1, args=(request))
			#t2 = threading.Thread(target=tr2, args=(request))
			#t3 = threading.Thread(target=getkey, args=(request))
			#t1.start()
			#t2.start()
			#t3.start()
			#t1.join()
			#t2.join()
			#t3.join()
			#print(request.session[str(request.user)])
			request.session[str(request.user)] = 1
			(request, val) = (list_users(request))
			return render(request, val)

@csrf_exempt
def getkey(request):
	c = {}
	c.update(csrf(request))
	arr = [2, 0]
	#t = Field.objects.get(field_id = request.session['field'])
	if(__main__.user1 == str(request.user)):
		while(__main__.request11 == 0):
			a = 0		
		if(__main__.request11 == 1):
			arr[0] = 1
			arr[1] = __main__.request12
			__main__.request11 = 0
			#t.save()
	else:
		while(__main__.request21 == 0):
			a = 0
		if(__main__.request21 == 1):
			arr[0] = 1
			arr[1] = __main__.request22
			__main__.request21 = 0
			#t.save()
	print threading.activeCount()
	return HttpResponse (json.dumps(arr), content_type="application/json")

@csrf_exempt
def tr2(request):
	c = {}
	c.update(csrf(request))
	#t = Field.objects.get(field_id = request.session['field'])
	if request.method == 'POST':
		POST = request.POST
		#t = Field.objects.get(field_id = request.session['field'])
		if(__main__.user2 == str(request.user)):
		#if(t.user2 == User.objects.get(username=str(request.user))):
			return __main__.newfield.Optreating(request)
		else:
			return __main__.oldfield.Optreating(request)
	#arr = [0, 0, 0, 0, 0]
	#return HttpResponse (json.dumps(arr), content_type="application/json")
	
@csrf_exempt
def tr1(request):
	c = {}
	c.update(csrf(request))
	#try:
	#	__main__.newfield.num = 0
	#except:
		#__main__.newfield = field()
		#__main__.newfield.createTank(120, 690)
	#	__main__.newfield.num = 0
	#t = Field.objects.get(field_id = request.session['field'])
	if request.method == 'POST':
		POST = request.POST
		if(__main__.user2 == str(request.user)):
		#if(t.user2 == User.objects.get(username=str(request.user))):
			__main__.request11 = 1
			__main__.request12 = POST['name']
			#t.save()
			return __main__.newfield.treating(request)
		else:
			__main__.request21 = 1
			__main__.request22 = POST['name']
			#t.save()
			return __main__.oldfield.treating(request)
	#arr = [0, 0, 0, 0, 0]
	#return HttpResponse (json.dumps(arr), content_type="application/json")

@csrf_exempt
def treating(request):
	c = {}
	c.update(csrf(request))
	__main__.newfield.num = 0
	return __main__.newfield.treating(request)

@csrf_exempt
def fl(request):
	c = {}
	c.update(csrf(request))
	t = Field.objects.get(field_id = request.session['field'])
	if request.method == 'POST':
		POST = request.POST
		if(t.user1 == str(request.user)):
			t.request11 = 1
			t.request12 = POST['name']
			t.save()
		else:
			t.request21 = 1
			t.request22 = POST['name']
			t.save()
	return __main__.newfield.flight(request)

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
def isend(request):
	c = {}
	c.update(csrf(request))
	POST = request.POST  
	if request.method == 'POST':
		if(__main__.live == 1):
			res = 0
		else:
			res = 1
		return HttpResponse (json.dumps(res), content_type="application/json")		

@csrf_exempt
def multiwin(request):
	c = {}
	c.update(csrf(request))
	__main__.live = 0
	t = Field.objects.filter(field_id = request.session['field'])
	t.delete()
	if request.method == 'POST':	
		return render(request,'webtanks/WIN.html')

@csrf_exempt
def win(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':	
		return render(request,'webtanks/WIN.html')

@csrf_exempt
def lose(request):
	c = {}
	c.update(csrf(request))
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
	if request.method == 'POST':
		if(__main__.user1 == str(request.user)):
			res = 0
		else:
			res = 1
		return HttpResponse (json.dumps(res), content_type="application/json")		


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
	#print(res)
	#if(t.state == 1):
	#	res = 1
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
		__main__.newfield.createTank(120, 120)
		__main__.newfield.createOpp(120, 690)
		__main__.newfield.num = 0
		request.session['field'] = u1
		return render(request, 'webtanks/connecting.html')

@csrf_exempt
def getsess(request):
	c = {}
	c.update(csrf(request))
	POST = request.POST  
	if request.method == 'POST':
		arr = [0, 0]
		arr[2] = str(request.user)
		arr[1] = __main__.ses
		return HttpResponse (json.dumps(arr), content_type="application/json")		

@csrf_exempt
def breakwall(request):
	c = {}
	c.update(csrf(request))	
	return __main__.newfield.breakwall(request)
	
@csrf_exempt
def oppbreakwall(request):
	c = {}
	c.update(csrf(request))
	#t = Field.objects.get(field_id = request.session['field'])
	if request.method == 'POST':
		POST = request.POST
		if(__main__.user2 == str(request.user)):
			return __main__.newfield.breakwall(request)
		else:
			return __main__.oldfield.breakwall(request)
