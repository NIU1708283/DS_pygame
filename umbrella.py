import pygame
import random
from pygame.locals import RLEACCEL

from screen import Screen
from game_sprite import GameSprite


class Umbrella(GameSprite):
    Min_Speed_y = 3
    Max_Speed_y = 8

    def __init__(self):
        super(Umbrella, self).__init__()
        # Asumimos que existe un 'icons/umbrella.png'
        self.surf = pygame.image.load("icons/umbrella.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        
        # Aparece en la parte superior, en una 'x' aleatoria
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, Screen.width),
                random.randint(-100, -20),
            )
        )
        self.speed_y = random.randint(self.Min_Speed_y, self.Max_Speed_y)

    def update(self):
        #""" Cae verticalmente """
        self.rect.move_ip(0, self.speed_y)
        # Se elimina si sale por la parte inferior
        if self.rect.top > Screen.height:
            self.kill()

    def clone(self):
        return Umbrella()