import pyxel
import instance.GameObject as GameObject
from Objects.Player.Player import Player
from Objects.Player.Shot import Shot
from Objects.Enemy.Enemy import Enemy
from Objects.Enemy.Boss import Boss
from Objects.Enemy.Bullet import Bullet
from Objects.Particle import Particle

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2
NUM_STARS = 100
STAR_COLOR_HIGH = 12
STAR_COLOR_LOW = 5


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

class Background:
    def __init__(self):
        self.stars = []
        for i in range(NUM_STARS):
            self.stars.append(
                (
                    pyxel.rndi(0, pyxel.width - 1),
                    pyxel.rndi(0, pyxel.height - 1),
                    pyxel.rndf(1, 2.5),
                )
            )

    def update(self):
        for i, (x, y, speed) in enumerate(self.stars):
            y += speed
            if y >= pyxel.height:
                y -= pyxel.height
            self.stars[i] = (x, y, speed)

    def draw(self):
        for (x, y, speed) in self.stars:
            pyxel.pset(x, y, STAR_COLOR_HIGH if speed > 1.8 else STAR_COLOR_LOW)



# 衝突判定
def overlaped(obj1, obj2):
	r1, r2 = obj1.size/2, obj2.size/2
	dx = abs(obj1.x - obj2.x)
	dy = abs(obj1.y - obj2.y)
	return dx < (r1 + r2) and dy < (r1 + r2)

press_enter = False

class App:
	def __init__(self):
		pyxel.init(160, 240, title="Test", fps=60)
		# self.init()
		self.scene = SCENE_TITLE
		self.press_enter = False
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
		self.score = 0
		self.background = Background()

	def update(self):
		
		if self.press_enter == False:
			return
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
		if self.scene == SCENE_TITLE:
			self.draw_title_scene()
			
			if pyxel.btnp(pyxel.KEY_RETURN) and self.press_enter == False:
				self.scene = self.scene+ 1
				self.press_enter = True
				self.init()
			return
		pyxel.cls(0)
		self.player.draw()
		Shot.mgr.draw()
		Enemy.mgr.draw()
		self.boss.draw()
		Bullet.mgr.draw()
		Particle.mgr.draw()
		# pyxel.cls(0)
		# self.background.draw()
		print(self.scene)
		# if self.scene == SCENE_TITLE:
		# 	self.draw_title_scene()
		# elif self.scene == SCENE_PLAY:
		# 	self.draw_play_scene()
		# elif self.scene == SCENE_GAMEOVER:
		# 	self.draw_gameover_scene()
		pyxel.text(39, 4, f"SCORE {self.score:5}", 7)

		if self.player.exists == False:
			pyxel.text(64, 100, "GAME OVER", 7)
			pyxel.text(48, 120, "Press 'R' to Restart", 7)

		if self.boss.exists == False:
			pyxel.text(48, 100, "MISSIN COMPLETE", 7)
			pyxel.text(40, 120, "Congratulations!!!", 7)

	def draw_title_scene(self):
		pyxel.text(35, 66, "Pyxel Shooter", pyxel.frame_count % 16)
		pyxel.text(31, 126, "- PRESS ENTER -", 13)
App()
