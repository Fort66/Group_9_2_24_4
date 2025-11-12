import pygame as pg
from pygame.locals import *
from pygame.image import load
from pygame.transform import scale, flip
from pygame import MOUSEMOTION
from pygame.mouse import get_pos, get_pressed
from pygame import Surface
from pygame.sprite import Sprite, Group

from sys import platform
from icecream import ic


pg.init()

class ButtonText(Sprite):
    """
    Класс для создания интерактивной кнопки с текстом в Pygame.

    Наследуется от `pygame.sprite.Sprite` и поддерживает события мыши,
    изменение цветов и вызов пользовательской функции при клике.

    Attributes:
        surface (Surface): Поверхность, на которой отрисовывается кнопка.
        pos (tuple): Центральная позиция кнопки (x, y).
        size (tuple or list): Ширина и высота кнопки.
        text (str): Текст, отображаемый на кнопке.
        font (Font): Объект шрифта Pygame.
        font_size (int): Размер шрифта.
        bg_color (str or tuple): Цвет фона кнопки.
        text_color (str or tuple): Цвет текста.
        hover_color (str or tuple): Цвет при наведении мыши.
        click_color (str or tuple): Цвет при нажатии.
        disabled_color (str or tuple): Цвет текста, когда кнопка отключена.
        disabled_text_color (str or tuple): Цвет текста, когда кнопка отключена.
        rounding (int): Радиус скругления углов кнопки.
        on_enabled (bool): Включена ли кнопка (реагирует на события).
        is_hovered (bool): Наведена ли мышь на кнопку.
        allow_clicking (bool): Разрешён ли клик (анти-спам).
        on_click (callable): Функция, вызываемая при клике.
        is_clicked (bool): Нажата ли кнопка.
        image (Surface): Поверхность кнопки с прозрачностью.
        rect (Rect): Прямоугольник для позиционирования и коллизий.
        mask_image (Surface): Маска для более точной отрисовки (не используется в текущей версии).
        mask_rect (Rect): Прямоугольник маски.
    """
    def __init__(self, surface=None, **kwargs):
        Sprite.__init__(self)
        self.surface = surface
        self.pos: tuple = kwargs.get('pos', (0, 0))
        self.size: list|tuple = kwargs.get('size', (50, 5))

        self.text: str = kwargs.get('text', 'Example')
        self.font: str = kwargs.get('font', None)
        self.font_size: int = kwargs.get('font_size', 26)

        self.disabled_color: str|tuple = kwargs.get('disabled_color','#2F4F4F')
        self.bg_color: str|tuple = kwargs.get('bg_color','#0B61A4')
        self.text_color: str|tuple = kwargs.get('text_color','#FFFFFF')
        self.disabled_text_color: str|tuple = kwargs.get('disabled_text_color','#FFFFFF')
        self.hover_color: str|tuple = kwargs.get('hover_color','#033E6B')
        self.click_color: str|tuple = kwargs.get('click_color','#66A3D2')
        self.color: str|tuple = kwargs.get('color', self.bg_color)

        self.rounding: int = kwargs.get('rounding',0)

        self.on_enabled: bool = kwargs.get('on_enabled', True)
        self.is_hovered: bool = kwargs.get('is_hovered', False)
        self.allow_clicking: bool = kwargs.get('allow_clicked', True)
        self.is_clicked: bool = kwargs.get('is_clicked', False)
        self.on_click: object = kwargs.get('on_click', lambda *args, **kwargs: None)

        self.image = Surface(self.size, pg.SRCALPHA)
        self.mask_image = self.image.copy().convert_alpha()
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=self.pos)
        self.mask_rect = self.mask_image.get_rect(center=self.rect.center)

        self.__post_init__(self)

    def __post_init__(self, font: str):
        if platform == 'win32':
            self.font = pg.font.Font(self.font, self.font_size) if self.font else pg.font.SysFont('Arial', self.font_size)

        elif platform == 'linux' or platform == 'linux2':
            self.font = pg.font.Font(self.font, self.font_size) if self.font else pg.font.SysFont('Arial', self.font_size)

        elif platform == 'darwin':
            self.font = pg.font.Font(self.font, self.font_size) if self.font else pg.font.SysFont('Sans-serif', self.font_size)

    def handleEvent(self):#, event):
        self.keys = get_pressed()
        if self.on_enabled:
            if MOUSEMOTION:
                self.is_hovered = self.rect.collidepoint(get_pos())

            if self.keys[0] and self.is_hovered:
                if self.allow_clicking and self.on_click:
                    self.is_clicked = True
                    self.on_click()
                    self.allow_clicking = False

            else:
                self.allow_clicking = True
                self.is_clicked = False


    def update(self):
        self.handleEvent()
        if self.on_enabled:
            if self.keys[0] and self.is_hovered:
                self.color = self.click_color
            elif self.is_hovered:
                self.color = self.hover_color
            else:
                self.color = self.bg_color
        else:
            self.color = self.disabled_color

        pg.draw.rect(self.surface, self.color, self.rect, border_radius = self.rounding)
        self.surface.blit(self.mask_image, self.rect)

        if self.text:
            if self.on_enabled:
                text_surface = self.font.render(self.text, True, self.text_color)
            else:
                text_surface = self.font.render(self.text, True, self.disabled_text_color)
                text_surface.fill(self.disabled_text_color, special_flags = pg.BLEND_RGBA_MULT)
            text_rect = text_surface.get_rect(center = self.rect.center)
            self.surface.blit(text_surface, text_rect)

