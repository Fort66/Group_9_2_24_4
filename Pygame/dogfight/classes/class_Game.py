import pygame as pg
pg.init()

from pygame.locals import QUIT, K_ESCAPE, KEYDOWN
from .class_Screen import win

from .class_Player import Player
from .class_Enemies import Enemies, enemies_group
from .class_Clouds import Clouds

from .all_sprites import all_sprites


player = Player()

clouds = [Clouds() for _ in range(15)]

class Game:
    def __init__(self):
        self.fps = 60
        self.clock = pg.time.Clock()
        self.loop = True
        self.setup()

    def setup(self):
        if len(enemies_group) < 15:
            enemies = [Enemies() for _ in range(15 - len(enemies_group))]

    def run(self):
        while self.loop:
            win.screen.fill('SkyBlue')


            for event in pg.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.loop = False

            self.setup()
            all_sprites.update()


            pg.display.update()
            self.clock.tick(self.fps)
