from django.shortcuts import render
from django.http import HttpResponse
from .field import field

def index(request):
	newfield = field()
	return render(request, 'webtanks/tanks.html')


def treating(request):
	if request.method == 'POST':
		POST = request.POST  
		if POST.name == 1:
			return HttpResponse (1);
		if POST.name == 2:
			return HttpResponse (1);
		if POST.name == 3:
			return HttpResponse (1);
		if POST.name == 4:
			return HttpResponse (1);
		return HttpResponse (2);
	else:
		return HttpResponse (0)

