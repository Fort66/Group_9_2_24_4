from pygame import Surface
from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale_by, flip


from ..screens.class_Screen import win



class PlayerShoots(Sprite):
    def __init__(self, pos, speed):
        Sprite.__init__(self)
        self.image = flip(scale_by(load('images/rocket.gif').convert_alpha(), .3), True, False)
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self._layer = 2

    def move(self):
        self.rect.move_ip(self.speed, 0)

    def check_position(self):
        if self.rect.right > win.screen.get_width() + 100:
            self.kill()

    def update(self):
        self.move()
        win.screen.blit(self.image, self.rect)