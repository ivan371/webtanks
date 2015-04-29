from django.http import HttpResponse
from django.core import serializers

def xhr_test(request):
    if request.is_ajax():
        if request.method == 'POST':
		POST = request.POST  
         	if POST.name(1):
			return HttpResponse(1);
           	if POST.name(2):
			return HttpResponse(1);
		if POST.name(3):
			return HttpResponse(1);
		if POST.name(4):
			return HttpResponse(1);
    else:
        return HttpResponse(status=400)
