from Settings import *
import pygame as p
class Player(p.sprite.Sprite):
    def __init__(self):
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface((TILESIZE, TILESIZE))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = 24
        self.rect.y = 24
        self.speedx = 0
        self.speedy = 0
    def update(self):
        self.speedx = 0
        key = p.key.get_pressed()
        if key[p.K_RIGHT]:
            self.speedx = 3
        if key[p.K_LEFT]:
            self.speedx = -3
        self.rect.x += self.speedx
player = Player()
