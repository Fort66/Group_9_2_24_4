from pygame.image import load
from pygame.transform import scale

from .class_Screen import win
from ..ui.class_ButtonText import ButtonText
from ..logic.class_Signals import signals
from ..logic.class_CreateObjects import create_objects


class StartScreen:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.image = scale(load('images/screens/start.jpg'), win.screen.get_size())
        self.rect = self.image.get_rect()

        self.btn = ButtonText(
            surface=self.image,
            pos=(
                self.rect[2] // 2,
                self.rect[3] - 200
            ),
            size=(200, 50),
            text='Начать игру',
            rounding=20,
            on_click=lambda: self.change_start()
        )

    def change_start(self):
        signals.change_signals('start')
        if self.btn.is_clicked:
            create_objects.create()

    def update(self):
        win.screen.blit(self.image, self.rect)
        self.btn.update()


start_screen = StartScreen()