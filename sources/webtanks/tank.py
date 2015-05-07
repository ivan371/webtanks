import math
from django.http import HttpResponse
from .bullet import bullet
import xml.etree.ElementTree as ET
import json

class tank:
	def __init__(self, X, Y):
		self.X = X
		self.Y = Y
		self.Xd = X + 24
		self.Yd = Y + 24
		self.begin()

	def begin(self):
		return HttpResponse (1, self.X, self.Y)

	def search_walls(self, kind):
		#1 - right, 2 - left, 3 - up, 4 - down
		if(kind == 1):
			tree = ET.parse('webtanks/static/wall_data/walls.xml')
			root = tree.getroot()
			vert = root.find('vertical')
			str = []
			for data in vert:
				for child in data:
	  				str.append(int(child.text))			
			for i in range(0, len(str), 3):
				#how far from the wall, how far from the begin, how far from the end
				if(math.fabs(self.X - str[i]) < 11 and str[i + 1] < self.Y and str[i + 2] + str[i + 1] > self.Y):
					return 0
			return 1
		if(kind == 2):
			tree = ET.parse('webtanks/static/wall_data/walls.xml')
			root = tree.getroot()
			vert = root.find('vertical')
			str = []
			for data in vert:
				for child in data:
	  				str.append(int(child.text))	
			for i in range(0, len(str), 3):
				if(math.fabs(self.Xd - str[i]) < 11 and str[i + 1] < self.Yd and str[i + 2] + str[i + 1] > self.Yd):
					return 0
			return 1
		if(kind == 3):
			tree = ET.parse('webtanks/static/wall_data/walls.xml')
			root = tree.getroot()
			vert = root.find('horizontal')
			str = []
			for data in vert:
				for child in data:
	  				str.append(int(child.text))	
			for i in range(0, len(str), 3):
				if(math.fabs(self.Yd - str[i]) < 11 and str[i + 1] < self.Xd and str[i + 2] + str[i + 1] > self.Xd):
					return 0
			return 1
		if(kind == 4):
			tree = ET.parse('webtanks/static/wall_data/walls.xml')
			root = tree.getroot()
			vert = root.find('horizontal')
			str = []
			for data in vert:
				for child in data:
	  				str.append(int(child.text))	
			for i in range(0, len(str), 3):
				if(math.fabs(self.Y - str[i]) < 11 and str[i + 1] < self.X and str[i + 2] + str[i + 1] > self.X):
					return 0
			return 1

	def treating(self, request):	
		arr = [0, 0, 0]
		if request.method == 'POST':
			POST = request.POST  
			if POST['name'] == '1':
				if(self.search_walls(1) == 1):
					self.X = self.X - 5
					self.Xd = self.Xd - 5
					arr[0] = 	1
					arr[1] = str(self.X)
					arr[2] = str(self.Y)
					return HttpResponse (json.dumps(arr),
            							content_type="application/json")
				else:
					return HttpResponse (json.dumps(arr),
            							content_type="application/json")
			if POST['name'] == '2':
				if(self.search_walls(2) == 1):
					self.X = self.X + 5
					self.Xd = self.Xd + 5
					arr[0] = 1
					arr[1] = self.X
					arr[2] = self.Y
					return HttpResponse (json.dumps(arr),
            							content_type="application/json")
				else:
					return HttpResponse (json.dumps(arr),
            							content_type="application/json")
			if POST['name'] == '3':
				if(self.search_walls(3) == 1):
					self.Y = self.Y + 5
					self.Yd = self.Yd + 5
					arr[0] = 1
					arr[1] = self.X
					arr[2] = self.Y
					return HttpResponse (json.dumps(arr),
            							content_type="application/json")
				else:
					return HttpResponse (json.dumps(arr),
            							content_type="application/json")			
			if POST['name'] == '4':
				if(self.search_walls(4) == 1):
					self.Y = self.Y - 5
					self.Yd = self.Yd - 5
					arr[0] = 1
					arr[1] = self.X
					arr[2] = self.Y
					return HttpResponse (json.dumps(arr),
            							content_type="application/json")		
				else:
					return HttpResponse (json.dumps(arr),
            							content_type="application/json")			
			return HttpResponse (json.dumps(arr),
            							content_type="application/json")		
		else:
			return HttpResponse (json.dumps(arr),
            							content_type="application/json")		

	
				
				
				
