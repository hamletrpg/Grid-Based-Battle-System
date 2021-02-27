import pygame as pg 
import pygame_gui
from utilities import *

class Gui:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.manager = pygame_gui.UIManager((WIDTH, HEIGHT))

    def update(self, time):
        self.manager.update(time)

    def draw(self, window):
        self.manager.draw_ui(window)

    def event(self, event):
        if event.type == pg.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                self.what_pressed()

        self.manager.process_events(event)

    def new_button(self, l, t, w, h, g_text):
        self.generic_button = pygame_gui.elements.UIButton(relative_rect=pg.Rect((l, t), (w, h)),
                                                            text = str(g_text),
                                                            manager = self.manager)

    def what_pressed(self):
        if self.generic_button.check_pressed():
            return self