import pygame
import random
from pygame.locals import RLEACCEL

from screen import Screen
from game_sprite import GameSprite


class Missile(GameSprite):
    Min_Speed = 15
    Max_Speed = 25

    def __init__(self):
        super(Missile, self).__init__()
        # Asumimos que existe un 'icons/missile.png'
        self.surf = pygame.image.load("icons/missile.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        
        self.rect = self.surf.get_rect(
            center=(
                random.randint(Screen.width + 20, Screen.width + 100),
                random.randint(0, Screen.height),
            )
        )
        self.speed = random.randint(self.Min_Speed, self.Max_Speed)

    def update(self):
        #""" Igual que el Jet, pero mucho más rápido """
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def clone(self):
        return Missile()