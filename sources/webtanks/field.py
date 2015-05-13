import xml.etree.ElementTree as ET
import os
from .tank import tank
from .bot import bot
from django.http import HttpResponse

#adding a new wall to the xml-file with information of walls
def createXML(kind, begin_length, begin_height, length):
		#kind: vertical, horizontal, breakvertical or breakhorizontal
		#begin_length - coordinate x of the beginning of the wall
		#begin_height - coordinate x of the beginning of the wall
		tree = ET.parse('webtanks/static/webtanks/xml/walls.xml')
		root = tree.getroot()
		a = root.find(kind)
		if kind == 'vertical':
			b = ET.SubElement(a, 'vert')
		if kind == 'horizontal':
			b = ET.SubElement(a, 'hor')
		if kind == 'breakvertical':
			b = ET.SubElement(a, 'breakver')
		if kind == 'breakhorizontal':
			b = ET.SubElement(a, 'breakhor')
		c = ET.SubElement(b, 'beginlength')
		c.text = begin_length
		c = ET.SubElement(b, 'beginheight')
		c.text = begin_height
		c = ET.SubElement(b, 'length')
		c.text = length
		tree.write('webtanks/static/webtanks/xml/walls.xml')

class field():
	def __init__(self):
		self.arrtank = []
		self.arrbots = []
		#deleting a previous version of xml-file with information about walls
		os.remove('webtanks/static/webtanks/xml/walls.xml')
		#creating a new version of xml-file
		root = ET.Element('root')
		a = ET.SubElement(root, 'vertical')
		a = ET.SubElement(root, 'horizontal')
		a = ET.SubElement(root, 'breakvertical')
		a = ET.SubElement(root, 'breakhorizontal')
		tree = ET.ElementTree(root)
		tree.write('webtanks/static/webtanks/xml/walls.xml')

		#adding new walls to the xml-file
		createXML('vertical', '100', '100', '620')
	
		createXML('vertical', '1024', '100', '620')

		createXML('horizontal', '100', '100', '924')

		createXML('horizontal', '720', '100', '924')

		createXML('horizontal', '200', '100', '724')
		createXML('vertical', '820', '175', '33')

		createXML('horizontal', '620', '300', '730')
		createXML('vertical', '310', '620', '33')

		createXML('vertical', '400', '300', '250')
		createXML('horizontal', '305', '403', '28')
		createXML('horizontal', '548', '375', '50')

		createXML('vertical', '700', '300', '250')
		createXML('horizontal', '305', '703', '28')
		createXML('horizontal', '548', '675', '50')

		createXML('breakvertical', '550', '206', '414')

		createXML('breakhorizontal', '200', '824', '294')		

		createXML('breakhorizontal', '620', '106', '200')

		createXML('breakhorizontal', '420', '106', '294')

		createXML('breakhorizontal', '420', '706', '312')

		self.num = 0
		self.bum = -1

	def bott(self, request):
		if request.method == 'POST':
			POST = request.POST 
		return self.arrbots[int(POST['num'])].bott(request)

	def treating(self, request):
		return self.arrtank[self.num].treating(request)

	def createTank(self, X, Y):
		newtank = tank(X, Y)
		self.arrtank.append(newtank)
		self.num = self.num + 1

	def createBot(self, X, Y):
		newbot = bot(X, Y, len(self.arrbots))
		self.arrbots.append(newbot)
		self.bum = self.bum + 1

	def flight(self, request):
		if request.method == 'POST':
			POST = request.POST
			if POST['who'] == '0': 
				return self.arrtank[self.num].flight(request)
			else:
				return self.arrbot[int(POST['who']) - 1].flightb(request)
