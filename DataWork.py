import pygame as pg 
import os 
from utilities import PIC_DICTIONARY, E_PIC_DICTIONARY

directory = os.path.join(os.path.dirname(__file__), "imgs")

def load_image(target, dirr, name):
    sprite = pg.image.load(os.path.join(directory, dirr + "/" + name)).convert()
    image = pg.Surface((target.w, target.h))
    image.blit(sprite, (1, 1))
    return image

def filled_up(dirr, var):
    character_quantity = [name for name in os.listdir(dirr)]
    for name in character_quantity:
        var.append(name)

def filled(dicts):
    for k, v in dicts.items():
        filled_up("imgs/" + k, v)

filled(PIC_DICTIONARY)
filled(E_PIC_DICTIONARY)