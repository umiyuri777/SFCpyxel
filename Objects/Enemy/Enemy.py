import math
import random
from instance.GameObject import GameObject
from Objects.Particle import Particle
from .Bullet import Bullet

class Enemy(GameObject):
	mgr = None
	target = None
	loop = 0
	@classmethod
	def add(cls, eid, x, y, deg, speed):
		obj = cls.mgr.add()
		if obj != None:
			obj.init(eid, x, y, deg, speed)
	def __init__(self):
		super().__init__()
		self.size = 12
		self.exists = False
	def init(self, eid, x, y, deg, speed):
		super().init(x, y, deg, speed)
		self.timer = 0
		self.eid = eid
		
		# データ定義
		dataTbl = [
		# hp, size, destroy
			[],
			[5, 12, 240, self.update1], # eid:1
			[1, 6, 240, self.update2], # eid:2
			[2, 4, 480, self.update3], # eid:3
			[5, 12, 240, self.update4], # eid:4
			[5, 12, 480, self.update5], # eid:5
			[5, 12, 240, self.update6], # eid:6
		]
		data = dataTbl[eid]
		self.hp = data[0]
		self.size = data[1]
		self.tDestroy = data[2]
		self.func = data[3]
		self.aim = 0
	def getAim(self):
		dx = self.target.x - self.x
		dy = self.target.y - self.y
		return math.degrees(math.atan2(-dy, dx))
	def bullet(self, deg, speed):
		# 弾を撃つ
		speed += Enemy.loop * 0.5 # ループするほど敵弾の速度が上がる
		Bullet.add(self.x, self.y, deg, speed)
	def bulletAim(self, ofs, speed):
		# 狙い撃ち弾
		aim = self.getAim()
		self.bullet(aim+ofs, speed)
	def dead(self):
		for i in range(8):
			deg = random.randrange(0, 360);
			speed = 1
			Particle.add(self.x, self.y, deg, speed, 11)
	def update(self):
		super().update()
		self.func()
		
		self.timer += 1
		if self.timer >= self.tDestroy:
			# 自爆
			self.hurt(999)
	def update1(self):
		self.vx *= 0.95
		self.vy *= 0.95
		for i in range(5):
			if self.timer%60 == (i*3)+40:
				if i == 0:
					self.aim = self.getAim()
				self.bullet(self.aim, 4)
	def update2(self):
		self.vx *= 0.97
		self.vy *= 0.97
		t = self.timer%120
		if t == 60 or t == 80 or t == 100:
#			for i in range(3):
			for i in range(1):
				aim = self.getAim() - 2 + 2*i
				self.bullet(aim, 0.5)
	def update3(self):
		self.vx *= 0.97
		self.vy *= 0.97
		if self.timer < 60:
			return
		if self.timer%75 == 0:
			self.bulletAim(0, 4)
	def update4(self):
		self.vx *= 0.95
		self.vy *= 0.95
		if self.timer < 60:
			return
		ofs = 20 * math.sin(math.radians(self.timer*2))
		self.bullet(270+ofs, 5)
	def update5(self):
		self.vx *= 0.95
		self.vy *= 0.95
		if self.timer < 60:
			return
		for i in range(10):
			if self.timer%60 == (i*3):
				if i == 0:
					self.aim = self.getAim()
				for i in range(3):
					self.bullet(self.aim-25+25*i, 3)
	def update6(self):
		self.vx *= 0.95
		self.vy *= 0.95
		if self.timer < 60:
			return
		self.bullet(120 + self.timer*7, 2)
	def draw(self):
		self.drawSelf(11)