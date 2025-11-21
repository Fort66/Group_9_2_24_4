from pygame.display import set_mode, set_caption, get_desktop_sizes
from pygame.locals import DOUBLEBUF


class Screen:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        # self.size = self.screen.get_size()
        # self.size = get_desktop_sizes()[0]
        self.size = ([1920, 1080])
        
        self.screen = set_mode(self.size, flags=DOUBLEBUF)
        self.caption = set_caption('My Game')
        self.rect = self.screen.get_rect()


win = Screen()