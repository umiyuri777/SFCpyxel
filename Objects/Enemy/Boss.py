import pyxel
from instance.GameObject import GameObject
from ..Particle import Particle
import random
from .Enemy import Enemy

# ボス
class Boss(GameObject):
	def __init__(self):
		super().__init__()
		self.size = 32
		self.timer = 0
		self.init(pyxel.width/2, 30, 0, 0)
		self.exists = True
		self.hp = 75
	def spawn(self, eid, deg, speed):
		Enemy.add(eid, self.x, self.y, deg, speed)
	def update(self):
		if self.exists == False:
			return;
		self.timer += 1
		t = self.timer
		if t == 60:
			self.spawn(1, 225, 2)
			self.spawn(1, 315, 2)
		if t%240 == 150:
			self.spawn(2, random.randrange(0, 360), 1)
		if t == 300:
			for i in range(20):
				self.spawn(3, i * 360/20, 1);
		if t == 440:
			self.spawn(4, 0, 2)
			self.spawn(4, 180, 2)
		if t == 600:
			self.spawn(5, 15, 2)
			self.spawn(5, 165, 2)
		if t == 760:
			self.spawn(6, 30, 2)
			self.spawn(6, 210, 2)
		if t == 900:
			# 最初に戻る
			self.timer = 0
			Enemy.loop += 1 # ループ回数をカウントアップ
	def dead(self):
		for i in range(32):
			deg = random.randrange(0, 360);
			speed = 0.1 + random.random() * 1.5
			Particle.add(self.x, self.y, deg, speed, 9)
	def draw(self):
		if self.exists == False:
			return;
		pyxel.text(self.x+24, self.y, "HP:%d"%self.hp, 7)
		self.drawSelf(9)
