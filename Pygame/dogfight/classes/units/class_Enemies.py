from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale_by

from random import uniform, randint

from ..screens.class_Screen import win
from ..groups.class_AllSprites import all_sprites
from ..groups.class_SpritesGroups import groups


class Enemies(Sprite):
    def __init__(self, path):
        Sprite.__init__(self)
        self.image = scale_by(load(path[0]).convert_alpha(), path[1])
        self.gen_pos()
        self.speed = randint(3, 5)
        self._layer = 2
        groups.enemies_group.add(self)
        all_sprites.add(self)

    def move(self):
        self.rect.move_ip(-self.speed, 0)

        if self.rect.left <= -1000:
            self.gen_pos()
        # else:
        #     # enemies_group.remove(self)
        #     if self in groups.enemies_group:
        #         self.kill()
        #     # if self in all_sprites:
        #         # all_sprites.remove(self)

    def gen_pos(self):
        self.rect = self.image.get_rect(center=(
            uniform(
                win.size[0] + 1000,
                win.size[0] + 5000
                ),
            uniform(
                0,
                win.size[1]
            )
        ))

    def update(self):
        self.move()
        win.screen.blit(self.image, self.rect)