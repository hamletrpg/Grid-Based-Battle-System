import pygame as pg
from utilities import *
from MoveCalc import *

class Character(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, color, atk, hp):
        pg.sprite.Sprite.__init__(self)
        self.atk = atk 
        self.hp = hp 
        self.w = w 
        self.h = h 
        self.name = NAME
        self.color = color 
        self.image = pg.Surface((w, h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.squares = []

    
    def show_posibilities_move(self, g):
        self.calculation = MoveCalc(self.rect.x, self.rect.y)
        for top, left in self.calculation.calc_movement(self):
            self.square = MoveCalc(top, left)
            self.all_sprites = pg.sprite.Group()
            self.all_sprites.add(self.square)
            self.all_sprites.draw(g)
            self.squares.append(self.square)

    def show_posibilities_attack(self, g):
        self.calculation = MoveCalc(self.rect.x, self.rect.y)
        for top, left in self.calculation.cal_attack_options(self):
            self.square = MoveCalc(top, left)
            self.all_sprites = pg.sprite.Group()
            self.all_sprites.add(self.square)
            self.all_sprites.draw(g)
            self.squares.append(self.square)