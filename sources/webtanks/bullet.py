import math
from django.http import HttpResponse
import json
from django.shortcuts import render_to_response
from .map import map

class bullet():
	def __init__(self, X, Y, kind, num, map):
		self.X = X
		self.Y = Y
		self.Xd = X + 6
		self.Yd = Y + 6
		self.kind = kind
		self.num = num
		self.map = map

	def search_solid_walls(self, kind):
		#1 - left, 2 - right, 3 - down, 4 - up
		if(kind == 1):
			for i in range(0, len(self.map.vertwall), 3):
				#how far from the wall, how far from the begin, how far from the end
				if(math.fabs(self.X - self.map.vertwall[i]) < 11 and self.map.vertwall[i + 1] <= self.Y and self.map.vertwall[i + 1] + self.map.vertwall[i + 2] >= self.Y):
					return 0
			return 1
		if(kind == 2):
			for i in range(0, len(self.map.vertwall), 3):
				if(math.fabs(self.Xd - self.map.vertwall[i]) < 11 and self.map.vertwall[i + 1] <= self.Yd and self.map.vertwall[i + 1] + self.map.vertwall[i + 2] >= self.Yd):
					return 0
			return 1
		if(kind == 3):
			for i in range(0, len(self.map.horwall), 3):
				if(math.fabs(self.Yd - self.map.horwall[i]) < 11 and self.map.horwall[i + 1] <= self.Xd and self.map.horwall[i + 1] + self.map.horwall[i + 2] >= self.Xd):
					return 0
			return 1
		if(kind == 4):
			for i in range(0, len(self.map.horwall), 3):
				if(math.fabs(self.Y - self.map.horwall[i]) < 11 and self.map.horwall[i + 1] <= self.X and self.map.horwall[i + 1] + self.map.horwall[i + 2] >= self.Xd):
					return 0
			return 1

	#tank is workind with durable walls
	def search_break_walls_for_tank(self, kind):
		#1 - left, 2 - right, 3 - down, 4 - up
		if(kind == 1):
			for i in range(0, len(self.map.breakvertwall), 3):
				#how far from the wall, how far from the begin, how far from the end
				if(math.fabs(self.X - self.map.breakvertwall[i]) < 11 and self.map.breakvertwall[i + 1] <= self.Yd and self.map.breakvertwall[i + 1] + self.map.breakvertwall[i + 2] >= self.Yd):
					return 0
			return 1
		if(kind == 2):
			for i in range(0, len(self.map.breakvertwall), 3):
				if(math.fabs(self.Xd - self.map.breakvertwall[i]) < 11 and self.map.breakvertwall[i + 1] <= self.Yd and self.map.breakvertwall[i + 1] + self.map.breakvertwall[i + 2] >= self.Yd):
					return 0
			return 1
		if(kind == 3):
			for i in range(0, len(self.map.breakhorwall), 3):
				if(math.fabs(self.Yd - self.map.breakhorwall[i]) < 11 and self.map.breakhorwall[i + 1] <= self.X and self.map.breakhorwall[i + 1] + self.map.breakhorwall[i + 2] >= self.Xd):
					return 0
			return 1
		if(kind == 4):
			for i in range(0, len(self.map.breakhorwall), 3):
				if(math.fabs(self.Y - self.map.breakhorwall[i]) < 11 and self.map.breakhorwall[i + 1] <= self.X and self.map.breakhorwall[i + 1] + self.map.breakhorwall[i + 2] >= self.Xd):
					return 0
			return 1

	#bullet is workind with durable walls
	def search_break_walls_for_bullet(self, kind):
		#1 - left, 2 - right, 3 - down, 4 - up
		if(kind == 1):
			for i in range(0, len(self.map.breakvertwall), 3):
				#how far from the wall, how far from the begin, how far from the end
				if(math.fabs(self.X - self.map.breakvertwall[i]) < 9 and self.map.breakvertwall[i + 1] + 6 <= self.Y and self.map.breakvertwall[i + 1] + self.map.breakvertwall[i + 2] >= self.Yd + 6):
					return (1, i)
			return (5, 0)
		if(kind == 2):
			for i in range(0, len(self.map.breakvertwall), 3):
				if(math.fabs(self.Xd - self.map.breakvertwall[i]) < 10 and self.map.breakvertwall[i + 1] + 6 <= self.Y and self.map.breakvertwall[i + 1] + self.map.breakvertwall[i + 2] >= self.Yd + 6):
					return (2, i)
			return (5, 0)
		if(kind == 3):
			for i in range(0, len(self.map.breakhorwall), 3):
				if(math.fabs(self.Yd - self.map.breakhorwall[i]) < 6 and self.map.breakhorwall[i + 1] + 6 <= self.X and self.map.breakhorwall[i + 1] + self.map.breakhorwall[i + 2] >= self.Xd + 6):
					return (3, i)
			return (5, 0)
		if(kind == 4):
			for i in range(0, len(self.map.breakhorwall), 3):
				if(math.fabs(self.Y - self.map.breakhorwall[i]) < 10 and self.map.breakhorwall[i + 1] + 6 <= self.X and self.map.breakhorwall[i + 1] + self.map.breakhorwall[i + 2] >= self.Xd + 6):
					return (4, i)
			return (5, 0)

	def searchtanks(self, Xtanks, Ytanks):
		for i in range (len(Xtanks)):
				if self.X < Xtanks[i] + 24 and self.X > Xtanks[i] and self.Y < Ytanks[i] + 24 and self.Yd > Ytanks[i]:
					return i
		return -1
	
	def flight(self, Xtanks, Ytanks, sort):
		arr = [0, 0, 0, 0, 0, 0]
		t = self.search_break_walls_for_bullet(self.kind)
		(type, number) = t
		if (type != 5):
			if (type == 1 or type == 2):
				self.map.breakvertwall.append(self.map.breakvertwall[number])
				self.map.breakvertwall.append(self.Yd + 12)
				self.map.breakvertwall.append(self.map.breakvertwall[number + 1] + self.map.breakvertwall[number + 2] - self.Yd)
				self.map.breakvertwall[number + 2] = self.Yd - self.map.breakvertwall[number + 1] + 5
			if (type == 3 or type == 4):
				self.map.breakhorwall.append(self.map.breakhorwall[number])
				self.map.breakhorwall.append(self.Xd - 11)
				self.map.breakhorwall.append(self.map.breakhorwall[number + 1] + self.map.breakhorwall[number + 2] - self.Xd + 24)
				self.map.breakhorwall[number + 2] = self.Xd - self.map.breakhorwall[number + 1] + 5
			arr[4] = 1	
			arr[5] = self.kind		
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
			arr[4] = 2
		arr[1] = self.X
		arr[2] = self.Y
		arr[3] = self.num
		return HttpResponse (json.dumps(arr), content_type="application/json"), self.map
