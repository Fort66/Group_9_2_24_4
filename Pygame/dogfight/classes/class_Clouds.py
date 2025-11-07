from pygame import Surface
from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale_by


from .class_Screen import win

from random import uniform, randint, choice

from .all_sprites import all_sprites


clouds_list = [
    'images/cloud2.png',
    'images/cloud3.png',
    'images/cloud4.png',
    'images/cloud5.png'
]


class Clouds(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self._layer = randint(1, 3)
        match self._layer:
            case 1:
                self.scale_value = .4
            case 2:
                self.scale_value = .6
            case 3:
                self.scale_value = .8
        self.image = scale_by(load(choice(clouds_list)).convert_alpha(), self.scale_value)
        self.check_position()
        self.speed = randint(1, 2)
        all_sprites.add(self)

    def move(self):
        if self.rect.left > -2000:
            self.rect.move_ip(-self.speed, 0)
        else:
            self.check_position()

    def check_position(self):
        self.rect = self.image.get_rect(center=(
            uniform(
                win.screen.get_width() + 1000,
                win.screen.get_width() + 5000
                ),
            uniform(
                0,
                win.screen.get_height()
            )
        ))

    def update(self):
        self.move()
        win.screen.blit(self.image, self.rect)