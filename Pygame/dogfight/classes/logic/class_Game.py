import pygame as pg
# pg.init()

from pygame.locals import QUIT, K_ESCAPE, KEYDOWN, K_F2

from ..screens import win, start_screen, pause_screen
from ..groups import all_sprites, groups

from ..logic.class_Signals import signals



class Game:
    def __init__(self):
        self.fps = 60
        self.clock = pg.time.Clock()
        self.loop = True

    def clear_groups(self):
        groups.clear()
        all_sprites.empty()

    def run(self):
        while self.loop:
            win.screen.fill('SkyBlue')


            for event in pg.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.loop = False
                if event.type == KEYDOWN and event.key == K_F2:
                    signals.change_signals('pause')

            if signals.start:
                start_screen.update()

            elif signals.pause:
                pause_screen.update()

            else:
                all_sprites.update()


            pg.display.update()
            self.clock.tick(self.fps)
