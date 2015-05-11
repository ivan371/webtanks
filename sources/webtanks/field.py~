import xml.etree.ElementTree as ET
import os
from .tank import tank

def createXML(kind, begin_lenght, begin_height, lenght):
		tree = ET.parse('webtanks/static/wall_data/walls.xml')
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
		c = ET.SubElement(b, 'beginlenght')
		c.text = begin_lenght
		c = ET.SubElement(b, 'beginheight')
		c.text = begin_height
		c = ET.SubElement(b, 'lenght')
		c.text = lenght
		tree.write('webtanks/static/wall_data/walls.xml')

class field():
	def __init__(self):
		self.arrtank = []
		os.remove('webtanks/static/wall_data/walls.xml')
		root = ET.Element('root')
		a = ET.SubElement(root, 'vertical')
		a = ET.SubElement(root, 'horizontal')
		a = ET.SubElement(root, 'breakvertical')
		a = ET.SubElement(root, 'breakhorizontal')
		tree = ET.ElementTree(root)
		tree.write('webtanks/static/wall_data/walls.xml')

		createXML('vertical', '100', '100', '620')
		createXML('vertical', '1024', '100', '620')
		createXML('horizontal', '100', '100', '924')
		createXML('horizontal', '720', '100', '924')
		createXML('horizontal', '200', '100', '724')
		createXML('horizontal', '620', '300', '724')
		createXML('vertical', '400', '300', '250')
		createXML('vertical', '700', '300', '250')
		createXML('breakvertical', '550', '206', '414')
		createXML('breakhorizontal', '200', '824', '294')
		createXML('breakhorizontal', '620', '106', '200')
		createXML('breakhorizontal', '420', '106', '294')
		createXML('breakhorizontal', '420', '706', '312')
		self.num = 0
		
	def flight(self, request):
		return self.arrtank[self.num].flight(request)


	def treating(self, request):
		return self.arrtank[self.num].treating(request)



	def createTank(self, X, Y):
		newtank = tank(X, Y)
		self.arrtank.append(newtank)
