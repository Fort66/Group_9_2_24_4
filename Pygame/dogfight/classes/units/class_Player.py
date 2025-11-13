from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_s, K_a, K_d, K_c, K_k
from pygame.key import get_pressed
from pygame.image import load
from pygame.transform import scale_by, rotozoom
from pygame.sprite import Sprite, groupcollide
from pygame import Vector2

from time import time
from itertools import count

from ..screens.class_Screen import win
from ..groups.class_AllSprites import all_sprites
from ..groups.class_SpritesGroups import groups
from .class_PlayerShoots import PlayerShoots
from .class_Explosion import Explosion
from ..logic.class_Weapons import Weapons

from icecream import ic

weapons = Weapons()

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = scale_by(load('images/su-33.png').convert_alpha(), .2)
        self.image_rotation = self.image.copy()
        self.rect = self.image.get_rect(center=(
            win.screen.get_width() // 2, win.screen.get_height() // 2
        ))
        self.direction = Vector2(self.rect.center)
        self.speed = 8
        self.permission_shot = .5
        self.shot_time = 1
        self.is_cobra = False
        self.cobra_time = 1
        self.permission_cobra = .01
        self.cobra_cnt = count(0, 3)
        self.cnt = 0
        self.angle = 0
        self._layer = 2
        self.prepare_weapons()
        groups.player_group.add(self)
        all_sprites.add(self)

    def move(self):
        keys = get_pressed()
        if True in keys:
            if keys[K_UP] or keys[K_w]:
                self.rect.move_ip(0, -self.speed)
                self.image_rotation = self.image.copy()
                self.angle = 15
                self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
                self.rect = self.image_rotation.get_rect(center=self.rect.center)

            if keys[K_DOWN] or keys[K_s]:
                self.rect.move_ip(0, self.speed)
                self.image_rotation = self.image.copy()
                self.angle = -15
                self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
                self.rect = self.image_rotation.get_rect(center=self.rect.center)

            if keys[K_LEFT] or keys[K_a]:
                self.rect.move_ip(-self.speed, 0)

            if keys[K_RIGHT] or keys[K_d]:
                self.rect.move_ip(self.speed, 0)

            if keys[K_c]:
                value = self.pos_weapons_rotation()
                for pos in value:
                    if not self.shot_time:
                        self.shot_time = time()
                    if time() - self.shot_time >= self.permission_shot:
                        shoot = PlayerShoots(pos=pos, speed=15, angle=self.angle)
                        groups.player_shots_group.add(shoot)
                        all_sprites.add(shoot)
                        self.shot_time = time()

            if keys[K_k]:
                self.is_cobra = True
                if not self.cobra_time:
                    self.cobra_time = time()

                if self.cnt < 117:
                    self.cnt = next(self.cobra_cnt)
                    self.angle = self.cnt
                    self.cobra()
                else:
                    self.cobra_cnt = count(self.cnt, -3)
        else:
            if not self.is_cobra:
                self.angle = 0
                self.image_rotation = self.image.copy()
                self.image_rotation = rotozoom(self.image_rotation, 0, 1)
                self.rect = self.image_rotation.get_rect(center=self.rect.center)
            else:
                if not self.cobra_time:
                    self.cobra_time = time()
                if self.cnt > 0:
                    self.cnt = next(self.cobra_cnt)
                    self.angle = self.cnt
                    self.cobra()
                else:
                    self.is_cobra = False
                    self.cobra_cnt = count(0, 3)

    def prepare_weapons(self):
        weapons.load_weapons(obj=self, source=[[-46, 10]], angle=self.angle)

    def pos_weapons_rotation(self):
        return weapons.pos_rotation(self, self.angle)

    def cobra(self):
        if time() - self.cobra_time >= self.permission_cobra:
            self.image_rotation = self.image.copy()
            self.image_rotation = rotozoom(self.image_rotation, self.cnt, 1)
            self.rect = self.image_rotation.get_rect(center=self.rect.center)
            self.cobra_time = time()

    def check_position(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= win.screen.get_width():
            self.rect.right = win.screen.get_width()
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= win.screen.get_height():
            self.rect.bottom = win.screen.get_height()

    def collision(self):
        rocket_collide = groupcollide(groups.player_shots_group, groups.enemies_group, True, True)
        if rocket_collide:
            hits = list(rocket_collide.keys())[0]
            self.explosion_rocket = Explosion(hits.rect.center, 1)
            self.explosion_rocket.speed = hits.speed * -1

    def update(self):
        self.move()
        self.check_position()
        self.collision()
        win.screen.blit(self.image_rotation, self.rect)
        weapons.update_weapons(self, self.angle)