##
## Modules to Import
## 

import pygame as p
from Settings import *
from Sprites import *

##
##   Class for game.
##

class Game:
    def __init__(self):
        self.exit = False
        p.init()
        self.screen = p.display.set_mode((WIDTH, HEIGHT))
        p.display.set_caption("2D Rpg")
        p.key.set_repeat(500, 100)
    def gamestart(self):
        self.sprites = p.sprite.Group()
        self.player = Player()
        self.player.add(self.sprites)
    def run(self):
        while not self.exit:
            g.events()
            g.draw()
            g.update()
    def quit(self):
        p.quit()
        quit()
    def update(self):
        self.sprites.update()
        p.display.update()
    def draw(self):
        self.screen.fill(black)
        g.draw_grid()
        self.sprites.draw(self.screen)
    def start_screen(self):
        pass
    def end_screen(self):
        pass
    def events(self):
        for event in p.event.get():
            if event.type ==  p.QUIT:
                self.exit = True
                quit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_LEFT:
                    self.player.move(x=-1)
                if event.key == p.K_RIGHT:
                    self.player.move(x=1)
                if event.key == p.K_UP:
                    self.player.move(y=-1)
                if event.key == p.K_DOWN:
                    self.player.move(y=1)
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            p.draw.line(self.screen, lightgrey, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            p.draw.line(self.screen, lightgrey, (0, y), (WIDTH, y))
g = Game()

while 1:
    g.gamestart()
    g.run()

