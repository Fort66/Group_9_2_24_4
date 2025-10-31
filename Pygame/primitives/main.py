import pygame as pg

from math import pi

pg.init()

size = (1024, 768)

scr = pg.display.set_mode(size)
pg.display.set_caption('MyGame')


loop = True

while loop:
    # scr.fill('black')


    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False


    pg.draw.rect(scr, 'red', (100, 100, 100, 100), 1)
    pg.draw.line(scr, 'yellow', (50, 50), (250, 250), 1)
    pg.draw.aaline(scr, 'green', (250, 50), (50, 250))

    pg.draw.lines(scr, 'blue', True, [[200, 80], [200, 180], [300, 180]], 1)

    pg.draw.polygon(scr, 'white', [[300, 80], [300, 180], [400, 180], [30, 230]], 1)
    
    pg.draw.circle(scr, 'pink', (200, 200), 50, 1)
    pg.draw.ellipse(scr, 'orange', (300, 300, 100, 50), 1)
    
    pg.draw.arc(scr, 'purple', (400, 400, 100, 50), 0, pi / 2, 1)



    pg.display.update()

pg.quit()