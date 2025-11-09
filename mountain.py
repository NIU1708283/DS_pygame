import pygame
import random
from pygame.locals import RLEACCEL

from screen import Screen
from game_sprite import GameSprite


class Mountain(GameSprite):
    def __init__(self):
        super(Mountain, self).__init__()
        # Asumimos que existe un 'icons/mountain.png'
        self.surf = pygame.image.load("icons/mountain.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        
        # [cite_start]Aparece a la derecha, anclado a la parte inferior [cite: 253]
        self.rect = self.surf.get_rect(
            center=(
                random.randint(Screen.width + 20, Screen.width + 100),
                Screen.height - self.surf.get_height() // 2,
            )
        )
        self.speed = 2 # Más lento que las nubes

    def update(self):
        #""" Se mueve de derecha a izquierda, como las nubes pero más lento """
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def clone(self):
        return Mountain()