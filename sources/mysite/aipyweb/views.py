from django.shortcuts import render
from django.http import HttpResponse
from .field import field

def index(request):
    newfield = field()
    return render(request, 'aipyweb/newdrawtank.html')
    #file = open('aipyweb/newdrawtank.html', 'r')
    #return HttpResponse(file)
