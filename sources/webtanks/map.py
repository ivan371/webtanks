from django.http import HttpResponse
import json
import math

class map():
	def __init__(self):
		self.vertwall = []
		self.horwall = []
		self.breakvertwall = []
		self.breakhorwall = []
		
	def map1(self):
		#adding new walls to arrays
		self.vertwall.append(100)
		self.vertwall.append(100)
		self.vertwall.append(620)
		
		self.vertwall.append(1024)
		self.vertwall.append(100)
		self.vertwall.append(620)
		
		self.horwall.append(100)
		self.horwall.append(100)
		self.horwall.append(924)
		
		self.horwall.append(720)
		self.horwall.append(100)
		self.horwall.append(924)
		 
		self.horwall.append(200)
		self.horwall.append(100)
		self.horwall.append(724)
		self.vertwall.append(820)
		self.vertwall.append(195)
		self.vertwall.append(8)
		
		self.horwall.append(620)
		self.horwall.append(300)
		self.horwall.append(730)
		self.vertwall.append(310) 
		self.vertwall.append(618)
		self.vertwall.append(8)
		
		self.vertwall.append(400)
		self.vertwall.append(300)
		self.vertwall.append(250)
		self.horwall.append(305)
		self.horwall.append(380)
		self.horwall.append(30)
		self.horwall.append(548)
		self.horwall.append(385)
		self.horwall.append(25)
		
		self.vertwall.append(700)
		self.vertwall.append(300)
		self.vertwall.append(250)
		self.horwall.append(305)
		self.horwall.append(680)
		self.horwall.append(32)
		self.horwall.append(548)
		self.horwall.append(685)
		self.horwall.append(25)
		
		self.breakvertwall.append(550)
		self.breakvertwall.append(206)
		self.breakvertwall.append(414)
		
		self.breakhorwall.append(200)
		self.breakhorwall.append(824)
		self.breakhorwall.append(294)
		
		self.breakhorwall.append(620)
		self.breakhorwall.append(106)
		self.breakhorwall.append(220)
		
		self.breakhorwall.append(420)
		self.breakhorwall.append(106)
		self.breakhorwall.append(294)
		
		self.breakhorwall.append(420)
		self.breakhorwall.append(706)
		self.breakhorwall.append(312)
		
	#bullet is workind with durable walls
	def search_break_walls_for_bullet(self, kind, X, Y):
		Xd = X + 6
		Yd = Y + 6
		#1 - left, 2 - right, 3 - down, 4 - up
		if(kind == 1):
			for i in range(0, len(self.breakvertwall), 3):
				#how far from the wall, how far from the begin, how far from the end
				if(math.fabs(X - self.breakvertwall[i]) < 9 and self.breakvertwall[i + 1] + 6 <= Y and self.breakvertwall[i + 1] + self.breakvertwall[i + 2] >= Yd + 6):
					print 'BULleft', self.breakvertwall[i], self.breakvertwall[i+1], self.breakvertwall[i+2], '|', X, Y, '|', Xd, Yd
					return (1, i)
				return (0, 0)
		if(kind == 2):
			for i in range(0, len(self.breakvertwall), 3):
				if(math.fabs(Xd - self.breakvertwall[i]) < 10 and self.breakvertwall[i + 1] + 6 <= Y and self.breakvertwall[i + 1] + self.breakvertwall[i + 2] >= Yd + 6):
					print 'BULright', self.breakvertwall[i], self.breakvertwall[i+1], self.breakvertwall[i+2], '|', X, Y, '|', Xd, Yd
					return (2, i)
				return (0, 0)
		if(kind == 3):
			for i in range(0, len(self.breakhorwall), 3):
				if(math.fabs(Yd - self.breakhorwall[i]) < 6 and self.breakhorwall[i + 1] + 6 <= X and self.breakhorwall[i + 1] + self.breakhorwall[i + 2] >= Xd + 6):
					print 'BULdown', self.breakhorwall[i], self.breakhorwall[i+1], self.breakhorwall[i+2], '|', X, Y, '|', Xd, Yd
					return (3, i)
				return (0, 0)
		if(kind == 4):
			for i in range(0, len(self.breakhorwall), 3):
				if(math.fabs(Y - self.breakhorwall[i]) < 10 and self.breakhorwall[i + 1] + 6 <= X and self.breakhorwall[i + 1] + self.breakhorwall[i + 2] >= Xd + 6):
					print 'BULup', self.breakhorwall[i], self.breakhorwall[i+1], self.breakhorwall[i+2], '|', X, Y, '|', Xd, Yd
					return (4, i)
				return (0, 0)
	
	def breakwall(self, X, Y, kind):
		Xd = X + 6
		Yd = Y + 6
		t = self.search_break_walls_for_bullet(kind, X, Y)
		(type, number) = t
		if (type == 1 or type == 2):
			self.breakvertwall.append(self.breakvertwall[number])
			self.breakvertwall.append(Yd + 12)
			self.breakvertwall.append(self.breakvertwall[number + 1] + self.breakvertwall[number + 2] - Yd)
			print "vert", self.breakvertwall[number], Yd + 12, self.breakvertwall[number + 1] + self.breakvertwall[number + 2] - Yd
			self.breakvertwall[number + 2] = Yd - self.breakvertwall[number + 1] + 50
			print "vert", breakvertwall[number], breakvertwall[number+1], breakvertwall[number+2]
		if (type == 3 or type == 4):
			self.breakhorwall.append(self.breakhorwall[number])
			self.breakhorwall.append(Xd - 11)
			self.breakhorwall.append(self.breakhorwall[number + 1] + self.breakhorwall[number + 2] - Xd + 24)
			print "hor", self.breakhorwall[number], Xd - 11, self.breakhorwall[number + 1] + self.breakhorwall[number + 2] - Xd + 24
			self.breakhorwall[number + 2] = Xd - self.breakhorwall[number + 1] + 50
			print "hor", breakhorwall[number], breakhorwall[number+1], breakhorwall[number+2]
		res = [0, 0]
		return HttpResponse (json.dumps(res), content_type="application/json")
