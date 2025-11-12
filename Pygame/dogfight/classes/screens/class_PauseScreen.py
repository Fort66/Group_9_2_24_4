from pygame.image import load
from pygame.transform import scale

from .class_Screen import win
from ..ui.class_ButtonText import ButtonText
from ..logic.class_Signals import signals
from ..logic.class_CreateObjects import create_objects


class PauseScreen:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.image = scale(load('images/screens/pause.jpg'), win.screen.get_size())
        self.rect = self.image.get_rect()

        self.btn = ButtonText(
            surface=self.image,
            pos=(
                self.rect[2] // 2,
                self.rect[3] - 200
            ),
            size=(200, 50),
            text='F2 - продолжить',
            on_enabled=False
        )


    def update(self):
        win.screen.blit(self.image, self.rect)
        self.btn.update()


pause_screen = PauseScreen()