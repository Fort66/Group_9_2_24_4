from pygame import Surface
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_s, K_a, K_d, K_c
from pygame.key import get_pressed
from pygame.image import load
from pygame.transform import scale_by
from pygame.sprite import Sprite

from time import time

from .class_Screen import Screen
from .all_sprites import all_sprites
from .class_PlayerShoots import PlayerShoots

scr = Screen()

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        # self.image = Surface((50, 50))
        # self.image.fill('MidnightBlue')
        self.image = scale_by(load('images/su-33.png'), .2)
        self.rect = self.image.get_rect(center=(
            scr.screen.get_width() // 2, scr.screen.get_height() // 2
        ))
        self.speed = 10
        self.permission_shot = .5
        self.shot_time = 1
        all_sprites.add(self)

    def move(self):
        keys = get_pressed()
        if keys[K_UP] or keys[K_w]:
            self.rect.move_ip(0, -self.speed)

        if keys[K_DOWN] or keys[K_s]:
            self.rect.move_ip(0, self.speed)

        if keys[K_LEFT] or keys[K_a]:
            self.rect.move_ip(-self.speed, 0)

        if keys[K_RIGHT] or keys[K_d]:
            self.rect.move_ip(self.speed, 0)

        if keys[K_c]:
            if not self.shot_time:
                self.shot_time = time()
            if time() - self.shot_time >= self.permission_shot:
                shoot = PlayerShoots(self.rect.center, 15)
                all_sprites.add(shoot)
                self.shot_time = time()

    def check_position(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= scr.screen.get_width():
            self.rect.right = scr.screen.get_width()
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= scr.screen.get_height():
            self.rect.bottom = scr.screen.get_height()

    def update(self):
        self.move()
        self.check_position()
        scr.screen.blit(self.image, self.rect)