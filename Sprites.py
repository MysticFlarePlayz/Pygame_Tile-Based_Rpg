from Settings import *
import pygame as p
class Player(p.sprite.Sprite):
    def __init__(self):
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface((TILESIZE, TILESIZE))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.x = 24
        self.y = 24
    def move(self, x=0, y=0):
        self.x += x
        self.y += y
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y  * TILESIZE

