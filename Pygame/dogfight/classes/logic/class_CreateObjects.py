from random import choice

from ..units.class_Player import Player
from ..units.class_Enemies import Enemies
from ..units.class_Clouds import Clouds
from .class_LevelsGame import levels_game


clouds_list = [
    'images/clouds/cloud2.png',
    'images/clouds/cloud3.png',
    'images/clouds/cloud4.png',
    'images/clouds/cloud5.png'
]


enemies_list = [
    ['images/planes/plane1.png', .1],
    ['images/planes/plane2.png', .1],
    ['images/planes/plane3.png', .1],
    ['images/planes/plane4.png', .12],
    ['images/planes/plane5.png', .12],
    ['images/planes/hc1.png', .12],
    ['images/planes/hc2.png', .12],
]

class CreateObjects:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def create(self):
        self.player = Player()
        self.clouds = [Clouds(choice(clouds_list)) for _ in range(15)]
        self.enemies = [Enemies(choice(enemies_list)) for _ in range(levels_game.enemies_amount)]


create_objects = CreateObjects()
