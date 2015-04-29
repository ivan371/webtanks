from django.shortcuts import render
from .field import field

def index(request):
	newfield = field()
	return render(request, 'webtanks/tanks.html')
