from django.shortcuts import render
from django.http import HttpResponse
from .field import field
from .tank import tank
from .bullet import bullet
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf


def index(request):
	newfield = field()
	return render(request, 'webtanks/tanks.html')


def treating(request):
	try:	
		return newtank.treating(request)
	except:
		newtank = tank()
		return newtank.treating(request)

def flight(request):
	newbullet = bullet()
	return newbullet.flight(request)

