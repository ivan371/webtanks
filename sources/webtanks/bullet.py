import math
from django.http import HttpResponse
import xml.etree.ElementTree as ET
import json
from django.shortcuts import render_to_response

#adding a new wall to the xml-file with information of walls
def createXML(kind, begin_arg1, begin_arg2, length):
	#kind: vertical, horizontal, breakvertical or breakhorizontal
	#begin_length - coordinate x of the beginning of the wall
	#begin_height - coordinate x of the beginning of the wall
	tree = ET.parse('webtanks/static/webtanks/xml/walls.xml')
	root = tree.getroot()
	a = root.find(kind)
	if kind == 'vertical':
		b = ET.SubElement(a, 'vert')
		c = ET.SubElement(b, 'beginlength')
		c.text = begin_arg1
		c = ET.SubElement(b, 'beginheight')
		c.text = begin_arg2
		c = ET.SubElement(b, 'length')
		c.text = length
	if kind == 'horizontal':
		b = ET.SubElement(a, 'hor')
		c = ET.SubElement(b, 'beginheight')
		c.text = begin_arg1
		c = ET.SubElement(b, 'beginlength')
		c.text = begin_arg2
		c = ET.SubElement(b, 'length')
		c.text = length
	if kind == 'breakvertical':
		b = ET.SubElement(a, 'breakver')
		c = ET.SubElement(b, 'beginlength')
		c.text = begin_arg1
		c = ET.SubElement(b, 'beginheight')
		c.text = begin_arg2
		c = ET.SubElement(b, 'length')
		c.text = length
	if kind == 'breakhorizontal':
		b = ET.SubElement(a, 'breakhor')
		c = ET.SubElement(b, 'beginheight')
		c.text = begin_arg1
		c = ET.SubElement(b, 'beginlength')
		c.text = begin_arg2
		c = ET.SubElement(b, 'length')
		c.text = length
	tree.write('webtanks/static/webtanks/xml/walls.xml')

#creating a list of certain walls in the string
def walls_list(kind):
	tree = ET.parse('webtanks/static/webtanks/xml/walls.xml')
	root = tree.getroot()
	edge = root.find(kind)
	list = []
	for data in edge:
		for child in data:
			list.append(int(child.text))	
	return list


class bullet():
	def __init__(self, X, Y, kind, num):
		self.X = X
		self.Y = Y
		self.Xd = X + 6
		self.Yd = Y + 6
		self.kind = kind
		self.num = num

	def search_solid_walls(self, kind):
		#1 - left, 2 - right, 3 - down, 4 - up
		if(kind == 1):
			list = walls_list('vertical')
			for i in range(0, len(list), 3):
				#how far from the wall, how far from the begin, how far from the end
				if(math.fabs(self.X - list[i]) < 11 and list[i + 1] <= self.Y and list[i + 1] + list[i + 2] >= self.Y):
					return 0
			return 1
		if(kind == 2):
			list = walls_list('vertical')
			for i in range(0, len(list), 3):
				if(math.fabs(self.Xd - list[i]) < 11 and list[i + 1] <= self.Yd and list[i + 1] + list[i + 2] >= self.Yd):
					return 0
			return 1
		if(kind == 3):
			list = walls_list('horizontal')
			for i in range(0, len(list), 3):
				if(math.fabs(self.Yd - list[i]) < 11 and list[i + 1] <= self.Xd and list[i + 1] + list[i + 2] >= self.Xd):
					return 0
			return 1
		if(kind == 4):
			list = walls_list('horizontal')
			for i in range(0, len(list), 3):
				if(math.fabs(self.Y - list[i]) < 11 and list[i + 1] <= self.X and list[i + 1] + list[i + 2] >= self.Xd):
					return 0
			return 1

	#tank is workind with durable walls
	def search_break_walls_for_tank(self, kind):
		#1 - left, 2 - right, 3 - down, 4 - up
		if(kind == 1):
			list = walls_list('breakvertical')
			for i in range(0, len(list), 3):
				#how far from the wall, how far from the begin, how far from the end
				if(math.fabs(self.X - list[i]) < 11 and list[i + 1] <= self.Yd and list[i + 1] + list[i + 2] >= self.Yd):
					return 0
			return 1
		if(kind == 2):
			list = walls_list('breakvertical')
			for i in range(0, len(list), 3):
				if(math.fabs(self.Xd - list[i]) < 11 and list[i + 1] <= self.Yd and list[i + 1] + list[i + 2] >= self.Yd):
					return 0
			return 1
		if(kind == 3):
			list = walls_list('breakhorizontal')
			for i in range(0, len(list), 3):
				if(math.fabs(self.Yd - list[i]) < 11 and list[i + 1] <= self.X and list[i + 1] + list[i + 2] >= self.Xd):
					return 0
			return 1
		if(kind == 4):
			list = walls_list('breakhorizontal')
			for i in range(0, len(list), 3):
				if(math.fabs(self.Y - list[i]) < 11 and list[i + 1] <= self.X and list[i + 1] + list[i + 2] >= self.Xd):
					return 0
			return 1

	#bullet is workind with durable walls
	def search_break_walls_for_bullet(self, kind):
		#1 - left, 2 - right, 3 - down, 4 - up
		if(kind == 1):
			list = walls_list('breakvertical')
			for i in range(0, len(list), 3):
				#how far from the wall, how far from the begin, how far from the end
				if(math.fabs(self.X - list[i]) < 9 and list[i + 1] <= self.Y and list[i + 1] + list[i + 2] >= self.Y):
					return (0, 1, i // 3, list[i], list[i + 1], list[i + 2])
			return (1, 0, 0, 0, 0, 0)
		if(kind == 2):
			list = walls_list('breakvertical')
			for i in range(0, len(list), 3):
				if(math.fabs(self.Xd - list[i]) < 10 and list[i + 1] <= self.Yd and list[i + 1] + list[i + 2] >= self.Yd):
					return (0, 2, i // 3, list[i], list[i + 1], list[i + 2])
			return (1, 0, 0, 0, 0, 0)
		if(kind == 3):
			list = walls_list('breakhorizontal')
			for i in range(0, len(list), 3):
				if(math.fabs(self.Yd - list[i]) < 6 and list[i + 1] <= self.Xd and list[i + 1] + list[i + 2] >= self.Xd):
					return (0, 3, i // 3, list[i], list[i + 1], list[i + 2])
			return (1, 0, 0, 0, 0, 0)
		if(kind == 4):
			list = walls_list('breakhorizontal')
			for i in range(0, len(list), 3):
				if(math.fabs(self.Y - list[i]) < 10 and list[i + 1] <= self.X and list[i + 1] + list[i + 2] >= self.Xd):
					return (0, 4, i // 3, list[i], list[i + 1], list[i + 2])
			return (1, 0, 0, 0, 0, 0)


	def searchtanks(self, Xtanks, Ytanks):
		for i in range (len(Xtanks)):
				if self.X < Xtanks[i] + 24 and self.X > Xtanks[i] and self.Y < Ytanks[i] + 24 and self.Yd > Ytanks[i]:
					return i
		return -1
	
	def tankflight(self, Xtanks, Ytanks, sort):
		arr = [0, 0, 0, 0]
		'''res = self.searchtanks(Xtanks, Ytanks)
		if res != 1:
			arr[0] = 6
			arr[1] = res
			arr[2] = sort
			#bot 1; tank 0
			return HttpResponse (json.dumps(arr), content_type="application/json")'''
		t = self.search_break_walls_for_bullet(self.kind)
		(res, type, number, arg1, arg2, arg3) = t
		if (res == 0):
			if (type == 1 or type == 2):
				tree = ET.parse('webtanks/static/webtanks/xml/walls.xml')
				root = tree.getroot()
				edge = root.find('breakvertical')
				i = 0
				for data in edge:
					if (i == number):
						for child in data:
							if (child.text == str(arg3)):
								child.text = str(self.Yd - arg2 + 7)							
								tree.write('webtanks/static/webtanks/xml/walls.xml')
								createXML('breakvertical', str(arg1), str(self.Yd + 12), str(arg2 + arg3 - self.Yd))
								#createXML('breakhorizontal', str(self.Yd), str(arg1 - 10), '30')
					i = i + 1
			if (type == 3 or type == 4):
				tree = ET.parse('webtanks/static/webtanks/xml/walls.xml')
				root = tree.getroot()
				edge = root.find('breakhorizontal')
				i = 0
				for data in edge:
					if (i == number):
						for child in data:
							if (child.text == str(arg3)):
								child.text = str(self.Xd - arg2 + 7)								
								tree.write('webtanks/static/webtanks/xml/walls.xml')
								createXML('breakhorizontal', str(arg1), str(self.Xd - 11), str(arg2 + arg3 - self.Xd))
					i = i + 1
			return HttpResponse (json.dumps(arr), content_type="application/json")		
		elif (self.search_solid_walls(self.kind) == 1):
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

	def flight(self, Xtanks, Ytanks, sort):
		arr = [0, 0, 0, 0]
		res = self.searchtanks(Xtanks, Ytanks)
		print("haha")
		print(res)
		if res != -1:
			arr[0] = 6
			arr[1] = res
			arr[2] = sort
			#bot 1; tank 0
			return HttpResponse (json.dumps(arr), content_type="application/json")
		if (self.search_solid_walls(self.kind) == 1):
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
				
