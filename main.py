import pygame as pg
from utilities import *
from Player import * 
from Enemy import *
import os
from Label import * 

class Game:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True 
        self.generic_font = pg.font.SysFont(FRONT_NAME, FONT_SIZE)
        self.bg = pg.transform.scale(pg.image.load(os.path.join("bg.png")), (WIDTH, HEIGHT))

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player(*PLAYER_ATT.values())
        self.enemy = Enemy(*ENEMY_ATT.values())


        self.all_sprites.add(self.player)
        self.all_sprites.add(self.enemy)

        self.player.player_controller()

        self.name_label = Label(50, HEIGHT - 100, self.player.name)
        self.name_label_original = self.generic_font.render(str(self.name_label), 1, (BLACK))

        self.run()

    def run(self):
        self.playing = True 
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

    def update(self):
        self.player.update_controller(FPS)
        self.player.update()
        self.enemy.update()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
            self.running = False

            self.player.basic_attack(self.enemy, event)
            self.player.controller_event_handler(event)
            self.player.actions(event)

    def draw_grid(self):
        # Vertical lines
        for x in range(0, WIDTH, TILEZISE):
            pg.draw.line(self.screen, YELLOW, (x, 0), (x, HEIGHT))

        for y in range(0, HEIGHT, TILEZISE):
            pg.draw.line(self.screen, YELLOW, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.player.action_posibility(self.screen)
        self.player.controller_screen_draw(self.screen)

        self.screen.blit(self.name_label_original, (self.name_label.x, self.name_label.y))
        pg.display.flip()

g = Game()
while g.running:
    g.new()

pg.quit()