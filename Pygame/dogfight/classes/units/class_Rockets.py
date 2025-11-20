from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale_by

from random import uniform, randint

from ..screens.class_Screen import win
from ..groups.class_AllSprites import all_sprites
from ..groups.class_SpritesGroups import groups


class Rockets(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = scale_by(load('images/rocket.gif').convert_alpha(), .3)
        self.check_position()
        self.speed = randint(3, 8)
        self._layer = 2
        groups.enemies_shots_group.add(self)
        all_sprites.add(self)

    def move(self):
        if self.rect.left > -300:
            self.rect.move_ip(-self.speed, 0)
        else:
            # enemies_group.remove(self)
            if self in groups.enemies_shots_group:
                self.kill()
            # if self in all_sprites:
                # all_sprites.remove(self)
            self.check_position()

    def check_position(self):
        self.rect = self.image.get_rect(center=(
            uniform(
                win.screen.get_width() + 300,
                win.screen.get_width() + 1000
                ),
            uniform(
                0,
                win.screen.get_height()
            )
        ))

    def update(self):
        self.move()
        win.screen.blit(self.image, self.rect)