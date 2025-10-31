import pygame as pg
from pygame.display import set_mode, set_caption

from pygame.locals import QUIT, K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN

from random import choice

pg.init()

size = (1024, 768)

scr = set_mode(size)
set_caption('MyGame')

lst = ['red', 'green', 'blue', 'yellow', 'pink', 'orange', 'purple', 'black']

loop = True

while loop:
    # scr.fill('black')


    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

        # if event.type == KEYDOWN:
        #     my_key = event.key
        #     my_mod = event.mod
        #     print(f'Нажата клавиша {my_key} с модификатором {my_mod}')

        if event.type == MOUSEBUTTONDOWN:
            # my_pos = event.pos
            if event.button == 1:
                scr.fill(choice(lst))




    pg.display.update()