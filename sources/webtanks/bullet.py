import math
from django.http import HttpResponse
import xml.etree.ElementTree as ET
import json
from django.shortcuts import render_to_response

class bullet():
	def __init__(self, X, Y, kind, num):
		self.X = X
		self.Y = Y
		self.Xd = X + 6
		self.Yd = Y + 6
		self.kind = kind
		self.num = num

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

	def flight(self, kind):
		arr = [0, 0, 0, 0]
		if (self.search_walls(kind) == 1):
			if kind == 1:
				self.X = self.X - 5
				self.Xd = self.Xd - 5
			if kind == 2:
				self.X = self.X + 5
				self.Xd = self.Xd + 5
			if kind == 3:
				self.Y = self.Y + 5
				self.Yd = self.Yd + 5
			if kind == 4:
				self.Y = self.Y - 5
				self.Yd = self.Yd - 5
			arr[0] = 2
			arr[1] = self.X
			arr[2] = self.Y
			arr[3] = self.num
			return HttpResponse (json.dumps(arr),
            							content_type="application/json")
				
		else:
			return HttpResponse (json.dumps(arr),
            							content_type="application/json")
				
