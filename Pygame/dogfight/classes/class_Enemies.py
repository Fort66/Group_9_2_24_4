from pygame import Surface
from pygame.sprite import Sprite, Group
from pygame.image import load
from pygame.transform import scale_by


from .class_Screen import win

from random import uniform, randint

from .all_sprites import all_sprites

enemies_group = Group()

class Enemies(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = scale_by(load('images/rocket.gif').convert_alpha(), .3)
        self.check_position()
        self.speed = randint(5, 10)
        self._layer = 2
        enemies_group.add(self)
        all_sprites.add(self)

    def move(self):
        if self.rect.left > -100:
            self.rect.move_ip(-self.speed, 0)
        else:
            enemies_group.remove(self)
            self.check_position()

    def check_position(self):
        self.rect = self.image.get_rect(center=(
            uniform(
                win.screen.get_width(),
                win.screen.get_width() + 500
                ),
            uniform(
                0,
                win.screen.get_height()
            )
        ))

    def update(self):
        self.move()
        win.screen.blit(self.image, self.rect)