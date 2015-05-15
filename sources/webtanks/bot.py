from .tank import tank
import random
from django.http import HttpResponse
import json
from .bullet import bullet
import time

class bot(tank):
	def __init__(self, X, Y, num):
		self.X = X
		self.Y = Y
		self.Xd = X + 24
		self.Yd = Y + 24
		self.cur = 1
		self.flag = 0
		self.num = num
		self.arrbull = []

	def change(self):
		time.sleep(1)
		cur = random.randint(1, 4)
		if(self.search_solid_walls(cur) == 1):
			self.cur = cur
		else:
			if(cur == 1):
				self.cur = 2
			elif(cur == 2):	
				self.cur = 1
			elif(cur == 3):
				self.cur = 4
			else:
				self.cur = 3			
	def flightb(self, request, Xtanks, Ytanks):
		if request.method == 'POST':
			POST = request.POST  
		print(POST['name'])
		return self.arrbull[int(POST['name'])].flight(Xtanks, Ytanks, 1)

	def bott(self, request):
		arr = [0, 0, 0, 0, 0, 0, 0]
		if request.method == 'POST':
			POST = request.POST  
			if POST['name'] == '6':
				self.change()
				if(self.cur == 1):
					self.left()
				if(self.cur == 2):
					self.right()
				if(self.cur == 3):
					self.down()
				if(self.cur == 4):
					self.up()
				arr[0] = 4
				arr[1] = self.X
				arr[2] = self.Y
				arr[3] = self.cur
				arr[4] = self.num
			if POST['name'] == '5':
				print("lalal")
				if(self.flag == 1):
					slideX = -6
					slideY = 8
				if(self.flag == 2):
					slideX = 22
					slideY = 8
				if(self.flag == 3):
					slideX = 8
					slideY = 22
				if(self.flag == 4):
					slideX = 8
					slideY = -6
				arr[0] = 2
				arr[1] = self.X + slideX
				arr[2] = self.Y + slideY
				arr[3] = len(self.arrbull)
				arr[4] = self.X
				arr[5] = self.Y
				arr[6] = self.flag
				newbullet = bullet(self.X + slideX, self.Y + slideY, self.flag, len(self.arrbull))
				self.arrbull.append(newbullet)
		return HttpResponse (json.dumps(arr), content_type="application/json")
		#return HttpResponse(0)
