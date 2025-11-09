import pygame
import random
from pygame.locals import RLEACCEL

from screen import Screen
from game_sprite import GameSprite


class Jet(GameSprite):
    Min_Speed = 7
    Max_Speed = 12

    def __init__(self):
        super(Jet, self).__init__()
        # Asumimos que existe un 'icons/jet.png'
        self.surf = pygame.image.load("icons/jet.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        
        # 1. MODIFICADO: Aparece a la izquierda, fuera de la pantalla
        self.rect = self.surf.get_rect(
            center=(
                random.randint(-100, -20),
                random.randint(0, Screen.height),
            )
        )
        self.speed = random.randint(self.Min_Speed, self.Max_Speed)

    def update(self):
        # 2. MODIFICADO: Vuela horizontalmente de izquierda a derecha
        self.rect.move_ip(self.speed, 0)
        
        # 3. MODIFICADO: Se elimina si sale por el borde derecho
        if self.rect.left > Screen.width:
            self.kill()

    def clone(self):
        return Jet()