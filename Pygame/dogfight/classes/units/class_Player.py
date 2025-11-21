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
from .class_Shoots import Shoots
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
        self.speed = 5
        self.permission_shot = .5
        self.shot_time = 1
        self.is_cobra = 0
        self.cobra_time = 1
        self.permission_cobra = .5
        self.cobra_cnt = count(0, 3)
        self.cnt = 0
        self.angle = 0
        self.cobra_angle = 0
        self._layer = 2
        self.directX = 1
        self.prepare_weapons()
        groups.player_group.add(self)
        all_sprites.add(self)

    def move(self):
        keys = get_pressed()
        if True in keys:
            if keys[K_UP] or keys[K_w]:
                self.rect.move_ip(0, -self.speed)
                self.rotation(15)

            if keys[K_DOWN] or keys[K_s]:
                self.rect.move_ip(0, self.speed)
                self.rotation(-15)

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
                        shoot = Shoots(pos=pos, speed=15, angle=self.angle, owner=self)
                        groups.player_shots_group.add(shoot)
                        all_sprites.add(shoot)
                        self.shot_time = time()

            if keys[K_k]:
                if not self.is_cobra:
                    self.is_cobra = 1
                    next(self.cobra_cnt)

        else:
            if not self.is_cobra:
                self.rotation(0)

            else:
                if not self.cobra_time:
                    self.cobra_time = time()

                if self.cobra_angle < 117 and self.is_cobra == 1:
                    self.cnt = next(self.cobra_cnt)
                    self.cobra_angle = self.cnt
                    angle = self.cnt

                    if self.cobra_angle >= 117:
                        self.cobra_cnt = count(self.cnt, -3)
                        self.is_cobra = -1

                if self.cobra_angle >= 117 and self.is_cobra == -1:
                    self.cnt = next(self.cobra_cnt)
                    angle = self.cnt

                if self.cnt <= 0:
                    self.cobra_angle = 0
                    self.cobra_cnt = count(0, 3)
                    self.is_cobra = 0
                self.rotation(angle)
                self.cobra_time = time()

    def rotation(self, angle):
        self.image_rotation = self.image.copy()
        self.image_rotation = rotozoom(self.image_rotation, angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)

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
        rocket_collide = groupcollide(groups.enemies_group, groups.player_shots_group,  True, True)
        if rocket_collide:
            hits = list(rocket_collide.keys())[0]
            self.explosion_rocket = Explosion(pos=hits.rect.center, types=1,scale_value=.5)
            self.explosion_rocket.speed = hits.speed * -1

    def update(self):
        self.move()
        self.check_position()
        self.collision()
        win.screen.blit(self.image_rotation, self.rect)
        weapons.update_weapons(self, self.angle)