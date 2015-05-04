import math
from django.http import HttpResponse
from .bullet import bullet

class tank():
	def __init__(self):
		self.X = 120
		self.Y = 690

	def search_walls(self, kind):
		#1 - right, 2 - left, 3 - up, 4 - down
		if(kind == 1):
			file = open('webtanks/wall_data/f_vertical.txt', 'r')
			str = []
			#write all data to the array
			for line in file.readlines():
				str.append(int(line))
			file.close()			
			for i in range(0, len(str), 3):
				#how far from the wall, how far from the begin, how far from the end
				if(math.fabs(self.X - str[i]) < 11 and str[i + 1] < self.Y and str[i + 2] + str[i + 1] > self.Y):
					return 0
			return 1
		if(kind == 2):
			file = open('webtanks/wall_data/f_vertical.txt', 'r')
			str = []
			for line in file.readlines():
				str.append(int(line))
			file.close()
			for i in range(0, len(str), 3):
				if(self.X - str[i] > 20 and self.X - str[i] < 25 and str[i + 1] < self.Y and str[i + 2] + str[i + 1] > self.Y):
					return 0
			return 1
		if(kind == 3):
			file = open('webtanks/wall_data/f_horizontal.txt', 'r')
			str = []
			for line in file.readlines():
				str.append(int(line))
			file.close()
			for i in range(0, len(str), 3):
				if(self.Y - str[i] and self.Y - str[i] < 25 and str[i + 1] < self.X and str[i + 2] + str[i + 1] > self.X):
					return 0
			return 1
		if(kind == 4):
			file = open('webtanks/wall_data/f_horizontal.txt', 'r')
			str = []
			for line in file.readlines():
				str.append(int(line))
			file.close()		
			for i in range(0, len(str), 3):
				if(math.fabs(self.Y - str[i]) < 11 and str[i + 1] < self.X and str[i + 2] + str[i + 1] > self.X):
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
				if(self.search_walls(2) == 1):
					self.X = self.X + 5
					return HttpResponse (1)
				else:
					return HttpResponse (2)
			if GET['name'] == '3':
				if(self.search_walls(3) == 1):
					self.Y = self.Y + 5
					return HttpResponse (1)
				else:
					return HttpResponse (2)			
			if GET['name'] == '4':
				if(self.search_walls(4) == 1):
					self.Y = self.Y - 5
					return HttpResponse (1)
				else:
					return HttpResponse (2)			
			return HttpResponse (2);
		else:
			return HttpResponse (0)

	
				
				
				
