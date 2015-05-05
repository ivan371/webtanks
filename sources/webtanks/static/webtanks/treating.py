from django.http import HttpResponse
from django.core import serializers

def xhr_test(request):
         if request.method == 'POST':
		POST = request.POST  
         	if POST.name == 1:
			return HttpResponse (1)
           	if POST.name == 2:
			return 1;
		if POST.name == 3:
			return 1;
		if POST.name == 4:
			return 1;
		return 2;
 	else:
        	return 0;


