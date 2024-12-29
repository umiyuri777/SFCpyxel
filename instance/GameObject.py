import math
import pyxel

class GameObject:
	def __init__(self):
		self.exists = False
		self.x = 0
		self.y = 0
		self.vx = 0
		self.vy = 0
		self.size = 6
		self.hp = 1
	def init(self, x, y, deg, speed):
		self.x, self.y = x, y
		rad = math.radians(deg)
		self.setSpeed(rad, speed)
	def move(self):
		self.x += self.vx
		self.y += self.vy
	def setSpeed(self, rad, speed):
		self.vx, self.vy = speed * math.cos(rad), speed * -math.sin(rad)
	def drawSelf(self, palette):
		pyxel.circ(self.x, self.y, self.size // 2, palette)
	def isOutSide(self):
		r2 = self.size // 2
		return self.x < -r2 or self.y < -r2 or self.x > pyxel.width+r2 or self.y > pyxel.height+r2
	def clipScreen(self):
		r2 = self.size // 2
		self.x = r2 if self.x < r2 else self.x
		self.y = r2 if self.y < r2 else self.y
		self.x = pyxel.width-r2 if self.x > pyxel.width-r2 else self.x
		self.y = pyxel.height-r2 if self.y > pyxel.height-r2 else self.y
	def update(self):
		self.move()
		if self.isOutSide():
			self.exists = False
	def dead(self):
		pass
	def hurt(self, val=1):
		if self.exists == False:
			return
		self.hp -= val
		if self.hp <= 0:
			self.exists = False
			self.dead()