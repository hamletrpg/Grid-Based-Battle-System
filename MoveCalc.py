import pygame as pg 
from utilities import *

class MoveCalc(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32, 32))
        self.image.fill(LIGHTYELLOW)
        self.image.set_alpha(128)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 

    def calc_movement(self, target):
        coordinates = []

        for k, v in POSSIBLE_MOVEMENTS.items():

            if k == "top":
                for _ in range(0, len(v)):
                    self.rect.x = target.rect.x
                    self.rect.y -= TILEZISE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))
            
            elif k == "left":
                for _ in range(0, len(v)):
                    self.rect.x -= TILEZISE
                    self.rect.y = target.rect.y
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "right":
                self.rect.x = target.rect.x
                for _ in range(0, len(v)):
                    self.rect.x += TILEZISE
                    self.rect.y = target.rect.y
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "bottom":
                for _ in range(0, len(v)):
                    self.rect.x = target.rect.x
                    self.rect.y += TILEZISE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))
        
        return coordinates

    def cal_attack_options(self, target):
        coordinates = []

        for k, v in POSSIBLE_ATTACKS.items():

            if k == "top":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y

                for _ in range(0, len(v)):
                    self.rect.y -= TILEZISE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "top-right":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):

                    self.rect.x += TILEZISE
                    self.rect.y -= TILEZISE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "top-left":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):
                    self.rect.x -= TILEZISE
                    self.rect.y -= TILEZISE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "right":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):
                    self.rect.x -= TILEZISE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "left":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):
                    self.rect.x += TILEZISE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "bottom-right":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):
                    self.rect.y += TILEZISE
                    self.rect.x += TILEZISE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "bottom-left":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):
                    self.rect.y += TILEZISE
                    self.rect.x -= TILEZISE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

            elif k == "bottom":
                self.rect.x = target.rect.x
                self.rect.y = target.rect.y
                for _ in range(0, len(v)):
                    self.rect.y += TILEZISE
                    coordinates.append(tuple((self.rect.x, self.rect.y)))

        return coordinates