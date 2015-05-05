import xml.etree.ElementTree as ET
import os

def createXML(kind, begin_lenght, begin_height, lenght):

		tree = ET.parse('webtanks/wall_data/walls.xml')
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

		tree.write('webtanks/wall_data/walls.xml')

class field():
	def __init__(self):
		os.remove('webtanks/wall_data/walls.xml');
		f_v = open('webtanks/wall_data/f_vertical.txt', 'w')
		f_h = open('webtanks/wall_data/f_horizontal.txt', 'w')  
		f_bv = open('webtanks/wall_data/f_break_ver.txt', 'w')
		f_bh = open('webtanks/wall_data/f_break_hor.txt', 'w')  
		#f_v.write("100, 100, 620\n") #begin lenght, begin height, len  
		f_v.write("100\n")
		f_v.write("100\n")
		f_v.write("620\n")		
		#f_v.write("1024, 100, 620\n")
		f_v.write("1024\n")
		f_v.write("100\n")
		f_v.write("620\n")
		#f_h.write("100, 100, 924\n") #begin height, begin lenght, len
		f_h.write("100\n")
		f_h.write("100\n")
		f_h.write("924\n")		
		#f_h.write("720, 100, 924\n")
		f_h.write("720\n")
		f_h.write("100\n")
		f_h.write("924\n") 
		#f_h.write("200, 100, 724\n")
		f_h.write("200\n")
		f_h.write("100\n")
		f_h.write("724\n")		
		#f_h.write("620, 300, 724\n")
		f_h.write("620\n")
		f_h.write("300\n")
		f_h.write("724\n")		
		#f_v.write("400, 300, 250\n")
		f_v.write("400\n")
		f_v.write("300\n")
		f_v.write("250\n")
		#f_v.write("700, 300, 250\n")
		f_v.write("700\n")
		f_v.write("300\n")
		f_v.write("250\n")		
		#f_bv.write("550, 206, 414\n")
		f_bv.write("550\n")
		f_bv.write("206\n")
		f_bv.write("414\n")
		#f_bh.write("200, 824, 294\n")
		f_bh.write("200\n")
		f_bh.write("824\n")
		f_bh.write("294\n")
		#f_bh.write("620, 106, 200\n")
		f_bh.write("620\n")
		f_bh.write("106\n")
		f_bh.write("200\n")
		#f_bh.write("420, 106, 294\n")
		f_bh.write("420\n")
		f_bh.write("106\n")
		f_bh.write("294\n")
		#f_bh.write("420, 706, 312\n")
		f_bh.write("420\n")
		f_bh.write("706\n")
		f_bh.write("312\n")
		f_v.close()
		f_h.close()
		f_bv.close()
		f_bh.close()
	
		root = ET.Element('root')
		a = ET.SubElement(root, 'vertical')
		a = ET.SubElement(root, 'horizontal')
		a = ET.SubElement(root, 'breakvertical')
		a = ET.SubElement(root, 'breakhorizontal')
		tree = ET.ElementTree(root)
		tree.write('webtanks/wall_data/walls.xml')

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
	

		
