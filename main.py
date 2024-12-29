import pyxel
import instance.GameObject as GameObject
from Objects.Player.Player import Player
from Objects.Player.Shot import Shot
from Objects.Enemy.Enemy import Enemy
from Objects.Enemy.Boss import Boss
from Objects.Enemy.Bullet import Bullet
from Objects.Particle import Particle


# ゲームオブジェクト管理
class GameObjectManager:
	def __init__(self, num, obj):
		self.pool = []
		for i in range(0, num):
			self.pool.append(obj())
	def add(self):
		for obj in self.pool:
			if obj.exists == False:
				obj.exists = True
				return obj
		return None
	def update(self):
		for obj in self.pool:
			if obj.exists:
				obj.update()
	def draw(self):
		for obj in self.pool:
			if obj.exists:
				obj.draw()
	def vanish(self):
		for obj in self.pool:
			if obj.exists:
				obj.hurt(999)


# 衝突判定
def overlaped(obj1, obj2):
	r1, r2 = obj1.size/2, obj2.size/2
	dx = abs(obj1.x - obj2.x)
	dy = abs(obj1.y - obj2.y)
	return dx < (r1 + r2) and dy < (r1 + r2)

class App:
	def __init__(self):
		pyxel.init(160, 240, title="Test", fps=60)
		self.init()
		pyxel.run(self.update, self.draw)
		
	def init(self):
		self.player = Player()
		Shot.mgr = GameObjectManager(32, Shot)
		Enemy.mgr = GameObjectManager(32, Enemy)
		Enemy.target = self.player
		self.boss = Boss()
		Bullet.mgr = GameObjectManager(256, Bullet)
		Particle.mgr = GameObjectManager(256, Particle)
		Enemy.loop = 0
		
	def update(self):
		if pyxel.btnp(pyxel.KEY_1):
			pyxel.quit()
		if pyxel.btnp(pyxel.KEY_R):
			self.init()
			
		# 各種オブジェクトの更新
		self.player.update()
		Shot.mgr.update()
		Enemy.mgr.update()
		self.boss.update()
		Bullet.mgr.update()
		Particle.mgr.update()
		
		if self.boss.exists == False:
			return
		
		# 自弾と敵との当たり判定
		for s in Shot.mgr.pool:
			if s.exists == False:
				continue
			
			for e in Enemy.mgr.pool:
				if e.exists == False:
					continue
				if overlaped(s, e):
					s.hurt()
					e.hurt()
					break
			
			if overlaped(s, self.boss):
				s.hurt()
				self.boss.hurt()
				if self.boss.exists == False:
					# 敵と敵弾を全て消す
					Enemy.mgr.vanish()
					Bullet.mgr.vanish()
		# 自機と敵弾との当たり判定
		if self.boss.exists == True:
			for b in Bullet.mgr.pool:
				if overlaped(self.player, b):
					self.player.hurt()
	def draw(self):
		pyxel.cls(0)
		self.player.draw()
		Shot.mgr.draw()
		Enemy.mgr.draw()
		self.boss.draw()
		Bullet.mgr.draw()
		Particle.mgr.draw()

		if self.player.exists == False:
			pyxel.text(64, 100, "GAME OVER", 7)
			pyxel.text(48, 120, "Press 'R' to Restart", 7)
			
		if self.boss.exists == False:
			pyxel.text(48, 100, "MISSIN COMPLETE", 7)
			pyxel.text(40, 120, "Congratulations!!!", 7)
App()