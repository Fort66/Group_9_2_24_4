import pygame as pg
from pygame.locals import QUIT, K_ESCAPE, KEYDOWN
from .class_Screen import Screen

from .class_Player import Player
from .class_Enemies import Enemies

from .all_sprites import all_sprites

scr = Screen()

player = Player()

enemies = [Enemies() for _ in range(15)]

class Game:
    def __init__(self):
        self.fps = 60
        self.clock = pg.time.Clock()
        self.loop = True

    def run(self):
        while self.loop:
            scr.screen.fill('SkyBlue')


            for event in pg.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.loop = False

            all_sprites.update()


            pg.display.update()
            self.clock.tick(self.fps)
