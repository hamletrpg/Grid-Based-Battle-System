from Character import * 
import pygame as pg 
from Gui import * 
from utilities import * 
import State
from DataWork import load_image

class Player(Character):
    def __init__(self, x, y, w, h, color, atk, hp):
        super().__init__(x, y, w, h, color, atk, hp)
        self.__state = State.GameState()
        self.index = 0
        self.idle = []
        self.walk_front = []
        self.attacking = []
        self.load_images()
        # self.image = self.idle[0]
        self.elapsed = 0

    def load_images(self):
        for dirr, values in PIC_DICTIONARY.items():
            for value in values:
                if dirr == "Character_Idle":
                    self.idle.append(load_image(self, dirr, value))
                elif dirr == "Character_Walking_Front":
                    self.walk_front.append(load_image(self, dirr, value))
                elif dirr == "Character_Attack":
                    self.attacking.append(load_image(self, dirr, value))

    def animation(self):
        now = pg.time.get_ticks()
        if self.get_state() == "idle":
            if now - self.elapsed > 250:
                self.elapsed = now
                self.index += 1
                if self.index >= len(self.idle):
                    self.index = 0
                self.image = self.idle[self.index]
        elif self.get_state() == "moving":
            if now - self.elapsed > 250:
                self.elapsed = now
                self.index += 1
                if self.index >= len(self.walk_front):
                    self.index = 0
                self.image = self.walk_front[self.index]
        if self.get_state() == "attacking":
            if now - self.elapsed > 250:
                self.elapsed = now
                self.index += 1
                try:
                    if self.index >= len(self.attacking):
                        self.index = 0
                    self.image = self.attacking[self.index]
                except IndexError:
                    self.index = 0
        self.image.set_colorkey(BLACK)

    def update(self):
        self.animation()

    def player_controller(self):
        self.attack_button = Gui()
        self.walk_button = Gui()
        self.change_button = Gui()

        self.attack_button.new_button(WIDTH - 80, HEIGHT - 80, 64, 64, "Attack")
        self.walk_button.new_button(WIDTH - 150, HEIGHT - 80, 64, 64, "Walk")
        self.change_button.new_button(WIDTH - 215, HEIGHT - 80, 64, 64, "Change")

    def actions(self, event):
        self.mouse_rect_init = pg.Surface((self.w, self.h))
        self.mouse_rect = self.mouse_rect_init.get_rect()
        self.mouse_rect.x, self.mouse_rect.y = pg.mouse.get_pos()
        for squa in self.squares:
            if event.type == pg.MOUSEBUTTONDOWN and squa.rect.collidepoint(self.mouse_rect.x, self.mouse_rect.y) and self.get_state() == "moving":
                self.rect.x = squa.rect.x
                self.rect.y = squa.rect.y
                self.squares.clear()
                self.set_idle()

    def update_controller(self, frame):
        self.attack_button.update(frame)
        self.walk_button.update(frame)
        self.change_button.update(frame)
        self.switch()

    def controller_event_handler(self, event):
        self.attack_button.event(event)
        self.walk_button.event(event)
        self.change_button.event(event)

    def controller_screen_draw(self, screen):
        self.attack_button.draw(screen)
        self.walk_button.draw(screen)
        self.change_button.draw(screen)

    def action_posibility(self, screen):
        if self.get_state() == "attacking":
            self.show_posibilities_attack(screen)

        elif self.get_state() == "moving":
            self.show_posibilities_move(screen)

    def basic_attack(self, target, event):
        if self.get_state() == "attacking" and target:
            if event.type == pg.MOUSEBUTTONDOWN and target.rect.collidepoint(pg.mouse.get_pos()):
                raw_damage = target.hp - self.atk 
                target.hp = raw_damage
                print(target.hp)
                self.set_idle()

    def switch(self):
        for button in [self.attack_button, self.change_button, self.walk_button]:
            if button.what_pressed() == self.attack_button:
                self.set_fight()
            elif button.what_pressed() == self.walk_button:
                self.set_move()
            elif button.what_pressed() == self.change_button:
                self.set_idle()
    
    def set_idle(self):
        self.squares.clear()
        return self.__state.stop()

    def set_fight(self):
        return self.__state.fight()

    def set_move(self):
        return self.__state.walk()

    def get_state(self):
        return str(self.__state)