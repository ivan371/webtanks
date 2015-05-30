from .tank import tank
from .bullet import bullet

class opp(tank, bullet):
	def __init__(self, X, Y, mapp):
		#X and Y are initial coordinates of tank
		#self.X and self.Y are coordinates of left and upper point of tank 
		self.X = X
		self.Y = Y
		#self.Xd and self.Yd are coordinates of right and lower point of tank
		self.Xd = X + 24
		self.Yd = Y + 24	
		self.flag = 0
		self.arrbullet = []
		self.map = mapp
	
