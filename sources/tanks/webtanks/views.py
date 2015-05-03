from django.shortcuts import render
from django.http import HttpResponse
from .field import field
from .tank import tank
from .bullet import bullet
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
import __main__

def index(request):
	newfield = field()
	__main__.newtank = tank()
	return render(request, 'webtanks/tanks.html')


def treating(request):
	return __main__.newtank.treating(request)

def flight(request):
	newbullet = bullet()
	return newbullet.flight(request)

