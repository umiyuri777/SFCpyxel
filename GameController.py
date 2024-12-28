import pyxel
from InputDetector import InputDetector as Input
 
class App:
    def __init__(self):
        pyxel.init(160, 120, fps=60)
        self.x = 0
        self.y = 0
        pyxel.load("player.pyxres")
        pyxel.blt(0, 50, 0, 0, 0, 16, 16, 0)
        pyxel.run(self.update, self.draw)
 
    def update(self):
        # self.x = (self.x + 1) % pyxel.width
        if Input.is_pressed(Input.UP):
            self.y -= 1
        if Input.is_pressed(Input.DOWN):
            self.y += 1
        if Input.is_pressed(Input.LEFT):
            self.x -= 1
        if Input.is_pressed(Input.RIGHT):
            self.x += 1
 
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

        pyxel.blt(self.x, self.y + 50, 0, 0, 0, 16, 16, 0)
 
App()

print(App.x)