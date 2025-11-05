from pygame import Surface
from pygame.sprite import Sprite

from .class_Screen import Screen

scr = Screen()

class PlayerShoots(Sprite):
    def __init__(self, pos, speed):
        Sprite.__init__(self)
        self.image = Surface((25, 5))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def move(self):
        self.rect.move_ip(self.speed, 0)

    def check_position(self):
        if self.rect.right > scr.screen.get_width() + 100:
            self.kill()

    def update(self):
        self.move()
        scr.screen.blit(self.image, self.rect)