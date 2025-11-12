from random import choice

from ..units.class_Player import Player
from ..units.class_Enemies import Enemies
from ..units.class_Clouds import Clouds


clouds_list = [
    'images/clouds/cloud2.png',
    'images/clouds/cloud3.png',
    'images/clouds/cloud4.png',
    'images/clouds/cloud5.png'
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
        self.enemies = [Enemies() for _ in range(10)]


create_objects = CreateObjects()