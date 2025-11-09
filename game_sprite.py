import pygame
from abc import ABC, abstractmethod


class GameSprite(pygame.sprite.Sprite, ABC):
    """
    Clase base abstracta para todos los sprites del juego
    que se pueden clonar (Patrón Prototype).
    """
    def __init__(self):
        super(GameSprite, self).__init__()

    @abstractmethod
    def clone(self):
        """
        Devuelve una nueva instancia (un clon) del objeto.
        """
        pass

    @abstractmethod
    def update(self):
        """
        Actualiza la posición del sprite.
        """
        pass