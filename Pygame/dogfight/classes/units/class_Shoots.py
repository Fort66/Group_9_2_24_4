from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale_by, flip, rotozoom, rotate
from pygame import Vector2


from ..screens.class_Screen import win
from .class_Explosion import Explosion



class Shoots(Sprite):
    def __init__(self, pos, speed, angle, owner):
        Sprite.__init__(self)
        self.pos = Vector2(pos)
        self.offset = Vector2().rotate(angle)
        self.direction = Vector2(1, 0).rotate(-angle)

        if owner.directX > 0:
            self.image = flip(scale_by(load('images/rocket.gif').convert_alpha(), .3), True, False)
        else:
            self.image = scale_by(load('images/rocket.gif').convert_alpha(), .3)

        self.image_rotation = self.image.copy()
        self.image_rotation = rotozoom(self.image_rotation, angle, 1)
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.owner = owner
        self.old_shot_coordinate = Vector2(self.owner.rect.center)
        self._layer = 2
        self.kill_shot_distance = 2700

    def move(self):
        self.rect.move_ip(self.speed * self.owner.directX, 0)
        # self.pos += self.direction * self.speed
        # self.rect.center = self.pos

    def check_position(self):
        if (
            Vector2(self.rect.center).distance_to(self.old_shot_coordinate)
            > self.kill_shot_distance
        ):
            # distance_collision(self)
            self.kill()
            self.kill_rocket = Explosion(pos=self.rect.center, types=1, scale_value=.1)

    def update(self):
        self.check_position()
        self.move()
        win.screen.blit(self.image_rotation, self.rect)