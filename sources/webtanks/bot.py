from .tank import tank
import random
from django.http import HttpResponse
import json
from .bullet import bullet
import time

class bot(tank):
	def __init__(self, X, Y):
		self.X = X
		self.Y = Y
		self.Xd = X + 24
		self.Yd = Y + 24
		self.cur = 1
		self.flag = 0

	def change(self):
		time.sleep(0.1)
		cur = random.randint(1, 4)
		if(self.search_walls(cur) == 1):
			self.cur = cur
		else:
			self.cur = 5 - cur 

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
		print (list(arr))
		return HttpResponse (json.dumps(arr), content_type="application/json")
		#return HttpResponse(0)
