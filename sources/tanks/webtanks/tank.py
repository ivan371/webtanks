import math
from django.http import HttpResponse
from .bullet import bullet

class tank():
	def __init__(self):
		self.X = 120
		self.Y = 690

	def search_walls(self, kind):
		if(kind == 1):
			file = open('webtanks/wall_date/f_vertical.txt', 'r')
			str = []
			for line in file.readlines():
				str.append(int(line))
			for i in range(0, 3, len(str)/3):
				if(math.fabs(str[i] - self.X) < 5 and str[i + 1] < self.Y and str[i + 2] + str[i + 1] > self.Y):
					return 0
			return 1

	def treating(self, request):
		if request.method == 'GET':
			GET = request.GET  
			if GET['name'] == '1':
				if(self.search_walls(1) == 1):
					self.X = self.X - 5
					return HttpResponse (1)
				else:
					return HttpResponse (2)
			if GET['name'] == '2':
				self.X = self.X + 5
				return HttpResponse (1);
			if GET['name'] == '3':
				self.Y = self.Y + 5
				return HttpResponse (1);
			if GET['name'] == '4':
				self.Y = self.Y - 5
				return HttpResponse (1);
			return HttpResponse (2);
		else:
			return HttpResponse (0)

	
				
				
				
