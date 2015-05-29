from .tank import tank
from .bot import bot
from django.http import HttpResponse
from .map import map

class field(map):
	def __init__(self):
		self.arrtank = []
		self.arrbots = []
		self.map = map()
		self.map.map1()
		self.num = 0
		self.bum = -1
		self.numbul = 0
		self.Xbots = []
		self.Ybots = []
		self.Xtanks = []
		self.Ytanks = []
		self.bot = bot(0, 0, 0)

	def shot(self, request):
		if request.method == 'POST':
			return self.bot.shot(request)

	def bott(self, request):
		if request.method == 'POST':
			POST = request.POST 
		self.Xbots[int(POST['num'])] = self.arrbots[int(POST['num'])].X		
		self.Ybots[int(POST['num'])] = self.arrbots[int(POST['num'])].Y
		return self.arrbots[int(POST['num'])].bott(request)

	def treating(self, request):
		self.Xtanks[self.num] = self.arrtank[self.num].X		
		self.Ytanks[self.num] = self.arrtank[self.num].Y
		return self.arrtank[self.num].treating(request)

	def createTank(self, X, Y):
		newtank = tank(X, Y, self.map)
		self.arrtank.append(newtank)
		self.Xtanks.append(X)
		self.Ytanks.append(Y)
		self.num = self.num + 1
		
	def breakwall(self, request):
		if request.method == 'POST':
			POST = request.POST
			X = int(POST['X'])
			Y = int(POST['Y'])
			kind = int(POST['kind'])
			return self.map.breakwall(X, Y, kind)

	def createBot(self, X, Y):
		newbot = bot(X, Y, len(self.arrbots))
		self.arrbots.append(newbot)
		self.Xbots.append(X)
		self.Ybots.append(Y)
		self.bum = self.bum + 1

	def flight(self, request):
		if request.method == 'POST':
			POST = request.POST
			if POST['who'] == '0': 
				t = self.arrtank[self.num].flight(request, self.Xbots, self.Ybots)
				(tmp, self.map) = t
				return tmp
			else:	
				return self.bot.flightb(request, self.Xtanks, self.Ytanks)
				#return self.arrbots[int(POST['who']) - 1].flightb(request, self.Xtanks, self.Ytanks)
