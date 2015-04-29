from django.shortcuts import render
<<<<<<< HEAD
from .field import field

def index(request):
	newfield = field()
	return render(request, 'webtanks/tanks.html')
=======
from django.http import HttpResponse
from .field import field

def index(request):
    newfield = field()
    return render(request, 'aipyweb/newdrawtank.html')
    #file = open('aipyweb/newdrawtank.html', 'r')
    #return HttpResponse(file)
>>>>>>> 1a7ce2e7043b9ae5bf06962fad6c4dcf27f3b183
