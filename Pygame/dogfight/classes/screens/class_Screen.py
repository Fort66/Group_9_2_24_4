from pygame.display import set_mode, set_caption
from pygame.locals import DOUBLEBUF


class Screen:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.screen = set_mode([1920, 768], flags=DOUBLEBUF)
        self.rect = self.screen.get_rect()
        self.size = self.screen.get_size()
        self.caption = set_caption('My Game')


win = Screen()