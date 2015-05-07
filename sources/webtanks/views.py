from django.shortcuts import render
from django.http import HttpResponse
from .field import field
from .tank import tank
from .bullet import bullet
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
import __main__

def index(request):
	__main__.newfield = field()
	__main__.newfield.createTank(120, 690)
	#__main__.newtank = tank()
	return render(request, 'webtanks/newtanks.html')

@csrf_exempt
def treating(request):
	c = {}
    	c.update(csrf(request))
	__main__.newfield.num = 0
	return __main__.newfield.treating(request)

def flight(request):
	newbullet = bullet()
	return newbullet.flight(request)
