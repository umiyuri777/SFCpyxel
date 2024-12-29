from instance.GameObject import GameObject

class Particle(GameObject):
	mgr = None
	@classmethod
	def add(cls, x, y, deg, speed, palette):
		obj = cls.mgr.add()
		if obj != None:
			obj.init(x, y, deg, speed, palette)
	def __init__(self):
		super().__init__()
		self.size = 1
	def init(self, x, y, deg, speed, palette):
		super().init(x, y, deg, speed)
		self.palette = palette
		self.timer = 0
	def update(self):
		super().update()
		self.vx *= 0.97
		self.vy *= 0.97
		self.timer += 1
		if self.timer > 60:
			self.hurt(999)
	def dead(self):
		pass
	def draw(self):
		self.drawSelf(self.palette)