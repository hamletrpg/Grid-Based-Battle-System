TITLE = "Grid-Based Battle System"
WIDTH = 704
HEIGHT = 480
FPS = 60
FRONT_NAME = 'comicsans'
FONT_SIZE = 24

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
LIGHTYELLOW = (255,255,102)

TILEZISE = 32

NAME = "Cloud"

POSSIBLE_MOVEMENTS = {
    "top": [1, 1, 1, 1, 1],
    "left": [1, 1, 1, 1, 1],
    "right": [1, 1, 1, 1, 1],
    "bottom": [1, 1, 1, 1, 1]
}

POSSIBLE_ATTACKS = {
    "top": [1, 1, 1, 1, 1],
    "top-left": [1, 1, 1, 1, 1],
    "top-right": [1, 1, 1],
    "left": [1, 1, 1, 1, 1],
    "right": [1, 1, 1, 1, 1],
    "bottom": [1, 1, 1, 1, 1],
    "bottom-left": [1, 1, 1],
    "bottom-right": [1, 1]
}

PLAYER_ATT = {
    "x": 289,
    "y": 193,
    "w": 32,
    "h": 32,
    "color": GREEN,
    "atk": 25,
    "hp": 100
}

ENEMY_ATT = {
    "x": 289,
    "y": 33,
    "w": 32,
    "h": 32,
    "color": RED,
    "atk": 25,
    "hp": 100
}

PIC_DICTIONARY = {
    "Character_Idle": [],
    "Character_Walking_Front": [],
    "Character_Attack": []
}

E_PIC_DICTIONARY = {
    "Monster": []
}