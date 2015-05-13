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
		#1 - left, 2 - right, 3 - up, 4 - down
		if(kind == 1):
			tree = ET.parse('webtanks/static/webtanks/xml/walls.xml')
			root = tree.getroot()
			vert = root.find('vertical')
			str = []
			for data in vert:
				for child in data:
	  				str.append(int(child.text))			
			for i in range(0, len(str), 3):
				#how far from the wall, how far from the begin, how far from the end
				if(math.fabs(self.X - str[i]) < 11 and str[i + 1] < self.Y and str[i + 2] + str[i + 1] > self.Y): #Y
					print 'left', 'horizontal', str[i], str[i+1], str[i+2], '|', self.X, self.Y, '|', self.Xd, self.Yd
					return 0
			print 'left', self.X, self.Y, '|', self.Xd, self.Yd
			return 1
		if(kind == 2):
			tree = ET.parse('webtanks/static/webtanks/xml/walls.xml')
			root = tree.getroot()
			vert = root.find('vertical')
			str = []
			for data in vert:
				for child in data:
	  				str.append(int(child.text))	
			for i in range(0, len(str), 3):
				if(math.fabs(self.Xd - str[i]) < 11 and str[i + 1] < self.Yd and str[i + 2] + str[i + 1] > self.Y): #Yd
					print 'right', 'horizontal', str[i], str[i+1], str[i+2], '|', self.X, self.Y, '|', self.Xd, self.Yd
					return 0
			print 'right', self.X, self.Y, '|', self.Xd, self.Yd
			return 1
		if(kind == 3):
			tree = ET.parse('webtanks/static/webtanks/xml/walls.xml')
			root = tree.getroot()
			vert = root.find('horizontal')
			str = []
			for data in vert:
				for child in data:
	  				str.append(int(child.text))	
			for i in range(0, len(str), 3):
				if(math.fabs(self.Yd - str[i]) < 11 and str[i + 1] < self.Xd and str[i + 2] + str[i + 1] > self.Xd):
					print 'down', 'horizontal', str[i], str[i+1], str[i+2], '|', self.X, self.Y, '|', self.Xd, self.Yd
					return 0
			print 'down', self.X, self.Y, '|', self.Xd, self.Yd
			return 1
		if(kind == 4):
			tree = ET.parse('webtanks/static/webtanks/xml/walls.xml')
			root = tree.getroot()
			vert = root.find('horizontal')
			str = []
			for data in vert:
				for child in data:
	  				str.append(int(child.text))	
			for i in range(0, len(str), 3):
				if(math.fabs(self.Y - str[i]) < 11 and str[i + 1] < self.X and str[i + 2] + str[i + 1] > self.Xd):
					print 'up', 'horizontal', str[i], str[i+1], str[i+2], '|', self.X, self.Y, '|', self.Xd, self.Yd
					return 0
			print 'up', self.X, self.Y, '|', self.Xd, self.Yd
			return 1	

	def searchtanks(self, Xtanks, Ytanks):
		for i in range (len(Xtanks)):
			if self.X > Xtanks[i] and self.Xd < Xtanks[i] + 24:
				return i
			print(1)
		for i in range (len(Ytanks)):
			if self.Y > Ytanks[i] and self.Yd < Ytanks[i] + 24:
				return i
			print(1)
		return 1

	def flight(self, Xtanks, Ytanks, sort):
		arr = [0, 0, 0, 0]
		'''res = self.searchtanks(Xtanks, Ytanks)
		if res != 1:
			arr[0] = 6
			arr[1] = res
			arr[2] = sort
			#bot 1; tank 0
			return HttpResponse (json.dumps(arr), content_type="application/json")'''
		if (self.search_walls(self.kind) == 1):
			if self.kind == 1:
				self.X = self.X - 5
				self.Xd = self.Xd - 5
			if self.kind == 2:
				self.X = self.X + 5
				self.Xd = self.Xd + 5
			if self.kind == 3:
				self.Y = self.Y + 5
				self.Yd = self.Yd + 5
			if self.kind == 4:
				self.Y = self.Y - 5
				self.Yd = self.Yd - 5
			arr[0] = 3
			arr[1] = self.X
			arr[2] = self.Y
			arr[3] = self.num
			return HttpResponse (json.dumps(arr), content_type="application/json")
				
		else:
			return HttpResponse (json.dumps(arr), content_type="application/json")
				
