from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .field import field
from .tank import tank
from .bot import bot
from .bullet import bullet
#from .bot import bot
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import __main__
import random
import json


def index(request):
	#__main__.newfield = field()
	#__main__.newfield.createTank(120, 690)
	#__main__.newfield.createBot(120, 120)
	#__main__.newfield.createBot(120, 300)
	if not request.user.is_authenticated():
	        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
	#__main__.newfield.createTank(100, 390)
	#__main__.newtank = tank()
	#return render(request, 'webtanks/newtanks.html')
	return render(request, 'webtanks/params.html')
	#return HttpResponseRedirect('webtanks/params.html')

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
def numbots(request):
	c = {}
	c.update(csrf(request))
	POST = request.POST  
	if request.method == 'POST':
        	res = int(POST['num'])
		__main__.newfield = field()
		__main__.newfield.createTank(120, 690)
		__main__.res = res
		for i in range (res):
			__main__.newfield.createBot(random.randint(100, 1000), random.randint(100, 700))
		return render(request, 'webtanks/newtanks.html')

@csrf_exempt
def numbot(request):
	c = {}
	c.update(csrf(request))
	POST = request.POST  
	if request.method == 'POST':
		res = __main__.res
		return HttpResponse (json.dumps(res), content_type="application/json")		
