#!/usr/bin/python
# -*- coding: utf-8 -*- 
from .models import Rating
from .models import Field
from .users import UserModel
from django.shortcuts import render
from django.contrib.auth.models import User
import time
import json
from django.http import HttpResponse


class views_db():
	def create_users(self):
		f = open("webtanks/templates/webtanks/users.html", "w")
		f.write('{% extends "base.html" %}'
			"{% load staticfiles %}"
			"{% block title %}Выбор противника{% endblock %}"
			"{% block content %}"
			'<div style="display: table; margin: 0 auto; padding: 1em 0; text-align: center;">'
			'<label for=""num""><font size="6" color="black" face="Calibri">Список пользователей и их рейтинг: </font></label>'
			"</div>")
		t = Rating.objects.order_by("-rating")
		for result in t:
			f.write('<div style="display: table; margin: 0 auto; padding: 5px; text-align: center;"><font size="5" color="navy" face="Arial">')
			f.write(str(result.who))
			f.write(" - ")
			f.write(str(result.rating))
			f.write('</font>')
			f.write('</div>')

		f.write("<form action=""/webtanks/chmod/num/users/"" method=""post"">"
		'<div style="display: table; margin: 0 auto; padding: 1em 0; text-align: center;">'
		'<label for=""num""><font size="6" color="black" face="Calibri">Введите имя противника: </font></label>'
		"<input id=""num"" type=""text"" name=""num"">"
		"<input type=""submit"" value=""OK"">"
		"</form>"
		"</div>"
		"{% endblock %}")
		f.close
	
	def create_rating(self, request):
		f = open("webtanks/templates/webtanks/rating.html", "w")
		f.write('{% extends "base.html" %}'
			"{% load staticfiles %}"
			"{% block title %}Рейтинг{% endblock %}"
			"{% block content %}"
			'<div style="display: table; margin: 0 auto; padding: 1em 0; text-align: center;">'
			'<label for=""num""><font size="6" color="black" face="Calibri">')	
		f.write(str(request.user))
		f.write(', ваш рейтинг:</font></label>'
			"</div>")
		r = Rating.objects.filter(who = User.objects.get(username=str(request.user)))
		for result in r:
			f.write('<div style="display: table; margin: 0 auto; padding: 5px; text-align: center;"><font size="5" color="navy" face="Arial">')
			f.write(str(result.rating))
			f.write('</font>')
			f.write('</div>')
		f.write("</div>"
			"{% endblock %}")
		f.close
		
	def change_rating(self, request):
		try:
			Field.objects.get(field_id = request.session['field']).delete()
		except:
			a = 0
		f = Rating.objects.get(who = User.objects.get(username=str(request.user)))
		f.rating = f.rating + 100
		f.save()
		return render(request,'webtanks/WIN.html')

	def is_in_game(self, request):
		t = Field.objects.all()
		for result in t:
			if(str(result.user1) == str(request.user)):
				request.session['field'] = result.field_id
				result.state = 1
				result.save()
				return 1
		return 0
		
	def delete(self):
		try:
			Field.objects.get(field_id = request.session['field']).delete()
		except:
			a = 0
			
	def mkfield(self, request):
		POST = request.POST  
		if request.method == 'POST':
			u1 = int(time.mktime(time.gmtime()))
			user = User.objects.get(username=str(POST['num']))
			us = User.objects.get(username=str(request.user))
			f = Field(field_id = u1, user1 = user, user2 = us)
			f.save()
			request.session['field'] = u1
			
			
	def chooose(self, request):
		res = 0
		t = Field.objects.filter(field_id = request.session['field'])
		for r in t:
			if(r.state == 1):
				res = 1
		return HttpResponse (json.dumps(res), content_type="application/json")
	
