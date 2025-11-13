from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale_by, flip, rotozoom, rotate
from pygame import Vector2


from ..screens.class_Screen import win



class PlayerShoots(Sprite):
    def __init__(self, pos, speed, angle):
        Sprite.__init__(self)
        self.pos = Vector2(pos)
        self.offset = Vector2().rotate(angle)
        self.direction = Vector2(1, 0).rotate(-angle)
        self.image = flip(scale_by(load('images/rocket.gif').convert_alpha(), .3), True, False)
        self.image_rotation = self.image.copy()
        self.image_rotation = rotozoom(self.image_rotation, angle, 1)
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self._layer = 2

    def move(self):
        # self.rect.move_ip(self.speed, 0)
        self.pos += self.direction * self.speed
        self.rect.center = self.pos

    def check_position(self):
        if self.rect.right > win.screen.get_width() + 100:
            self.kill()

    def update(self):
        self.move()
        win.screen.blit(self.image_rotation, self.rect)