import gif_pygame as gif
from gif_pygame import load
from gif_pygame.transform import scale_by

from pygame.sprite import Sprite

from ..groups.class_AllSprites import all_sprites
from ..screens.class_Screen import win


class Explosion(Sprite):
    def __init__(self, pos, types, scale_value):
        Sprite.__init__(self)
        self.pos = pos
        self.types = types
        self._layer = 2
        self.speed = 0

        if types == 1:
            self.image = scale_by(load('images/explosions/rocket_explosion.gif', loops=0), scale_value, new_gif=True)
            # self.image = scale_by(self.image, .5, new_gif=True)

        self.rect = self.image.get_rect(center=self.pos)
        all_sprites.add(self)

    def move(self):
        self.rect.move_ip(self.speed, 0)

    def update(self):
        if not self.image._ended:
            self.image.render(win.screen, self.rect)
        else:
            self.kill()
        self.move()