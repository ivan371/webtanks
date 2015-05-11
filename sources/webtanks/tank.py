import math
from django.http import HttpResponse
from .bullet import bullet
import xml.etree.ElementTree as ET
import json

class tank:
	def __init__(self, X, Y):
		#X and Y are initial coordinates of tank
		#self.X and self.Y are coordinates of left and upper point of tank 
		self.X = X
		self.Y = Y
		#self.Xd and self.Yd are coordinates of right and lower point of tank
		self.Xd = X + 24
		self.Yd = Y + 24	
		self.flag = 0
		self.arrbullet = []

	#investigating a question about collision with a wall
	def search_walls(self, kind):
		#kind: 1 - left, 2 - right, 3 - down, 4 - up
		if(kind == 1):
			#collecting information about walls from xml-file
			tree = ET.parse('webtanks/static/wall_data/walls.xml')
			root = tree.getroot()
			vert = root.find('vertical')
			str = []
			#creating a string with information about the particular kind of walls
			for data in vert:
				for child in data:
	  				str.append(int(child.text))
			#investigating a question about collision with a wall: 0 - a collusion, 1 - no collusion
			for i in range(0, len(str), 3):
				#checking how far from the wall, how far from the beginning, how far from the end
				if(math.fabs(self.X - str[i]) < 11 and str[i + 1] <= self.Y and str[i + 1] + str[i + 2] >= self.Y):
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
				if(math.fabs(self.Xd - str[i]) < 11 and str[i + 1] <= self.Yd and str[i + 1] + str[i + 2] >= self.Yd):
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
				if(math.fabs(self.Yd - str[i]) < 11 and str[i + 1] <= self.Xd and str[i + 1] + str[i + 2] >= self.Xd):
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
				if(math.fabs(self.Y - str[i]) < 11 and str[i + 1] <= self.X and str[i + 1] + str[i + 2] >= self.Xd):
					return 0
			return 1

	def flight(self, request):
		if request.method == 'POST':
			POST = request.POST  
		print(POST['name'])
		return self.arrbullet[int(POST['name'])].flight()

	#receiving information from server about pressing keys
	def treating(self, request):	
		arr = [0, 0, 0, 0, 0, 0, 0]
		if request.method == 'POST':
			POST = request.POST  
			if POST['name'] == '1':
				if(self.search_walls(1) == 1):
					self.X = self.X - 5
					self.Xd = self.Xd - 5
					self.flag = 1
					arr[0] = 1
					arr[1] = self.X
					arr[2] = self.Y
					return HttpResponse (json.dumps(arr),
            							content_type="application/json")
				else:
					return HttpResponse (json.dumps(arr),
            							content_type="application/json")
			if POST['name'] == '2':
				if(self.search_walls(2) == 1):
					self.X = self.X + 5
					self.Xd = self.Xd + 5
					self.flag = 2
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
					self.flag = 3
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
					self.flag = 4
					arr[0] = 1
					arr[1] = self.X
					arr[2] = self.Y
					return HttpResponse (json.dumps(arr),
            							content_type="application/json")		
				else:
					return HttpResponse (json.dumps(arr),
            							content_type="application/json")
			if POST['name'] == '5':
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
				arr[3] = len(self.arrbullet)
				arr[4] = self.X
				arr[5] = self.Y
				arr[6] = self.flag
				newbullet = bullet(self.X + slideX, self.Y + slideY, self.flag, len(self.arrbullet))
				self.arrbullet.append(newbullet)
							
			return HttpResponse (json.dumps(arr),
            							content_type="application/json")		
		else:
			return HttpResponse (json.dumps(arr),
            							content_type="application/json")
