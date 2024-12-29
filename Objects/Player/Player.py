import pyxel
from instance.GameObject import GameObject
from ..Particle import Particle
import math
import random
from .Shot import Shot

class Player(GameObject):
	def __init__(self):
		super().__init__()
		self.x = pyxel.width/2
		self.y = pyxel.height*5/6
		self.size = 6
		self.exists = True
	def update(self):
		if self.exists == False:
			return
		
		if pyxel.btn(pyxel.KEY_SPACE):
			if pyxel.frame_count % 5 == 0:
				Shot.add(self.x, self.y, 90, 5) # 弾を撃つ
		
		# Moving...
		dx, dy = 0, 0
		if pyxel.btn(pyxel.KEY_A):
				dx = -1
		elif pyxel.btn(pyxel.KEY_D):
				dx = 1
		if pyxel.btn(pyxel.KEY_W):
				dy = -1
		elif pyxel.btn(pyxel.KEY_S):
				dy = 1
		if(dx == 0 and dy == 0):
			return # 動いていない
		rad = math.atan2(-dy, dx)
		speed = 2
		self.setSpeed(rad, speed)
		self.move()
		self.clipScreen()
	def dead(self):
		for i in range(32):
			deg = random.randrange(0, 360);
			speed = 0.1 + random.random() * 1.5
			Particle.add(self.x, self.y, deg, speed, 7)
	def draw(self):
		if self.exists == False:
			return
		self.drawSelf(7)
