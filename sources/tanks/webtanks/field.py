class field():
	def __init__(self):
<<<<<<< HEAD
		f_v = open('webtanks/wall_date/f_vertical.txt', 'w')
		f_h = open('webtanks/wall_date/f_break_hor.txt', 'w')  
		f_bv = open('webtanks/wall_date/f_break_ver.txt', 'w')
		f_bh = open('webtanks/wall_date/f_horisontal.txt', 'w')  
=======
		f_v = open('aipyweb/f_vertical.txt', 'w')
		f_h = open('aipyweb/f_break_hor.txt', 'w')  
		f_bv = open('aipyweb/f_break_ver.txt', 'w')
		f_bh = open('aipyweb/f_horisontal.txt', 'w')  
>>>>>>> 1a7ce2e7043b9ae5bf06962fad6c4dcf27f3b183
		f_v.write("100, 100, 620\n") #begin lenght, begin height, len  
		f_v.write("1024, 100, 620\n")
		f_h.write("100, 100, 924\n") #begin height, begin lenght, len
		f_h.write("720, 100, 924\n") 
		f_h.write("200, 100, 724\n")
		f_h.write("620, 300, 724\n")
		f_v.write("400, 300, 250\n")
		f_v.write("700, 300, 250\n")
		f_bv.write("550, 206, 414\n")
		f_bh.write("200, 824, 294\n")
		f_bh.write("620, 106, 200\n")
		f_bh.write("420, 106, 294\n")
		f_bh.write("420, 706, 312\n")
		f_v.close()
		f_h.close()
		f_bv.close()
		f_bh.close()
