from instance.GameObject import GameObject

class Bullet(GameObject):
	mgr = None
	@classmethod
	def add(cls, x, y, deg, speed):
		obj = cls.mgr.add()
		if obj != None:
			obj.init(x, y, deg, speed)
	def __init__(self):
		super().__init__()
		self.size = 4
	def dead(self):
		pass
	def draw(self):
		self.drawSelf(8)