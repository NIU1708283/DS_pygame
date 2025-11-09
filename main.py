import pygame
from game import Game
from screen import Screen

# Importamos todas las clases de sprites que usaremos como prototipos
from bird import Bird
from cloud import Cloud
from umbrella import Umbrella
from mountain import Mountain
from jet import Jet
from missile import Missile

# Importamos la fábrica
from factory_sprites import FactorySprites


# Initialize PyGame
# setup for sounds_music, defaults are good
pygame.mixer.init()
pygame.init()
# create the screen object
pygame.display.set_mode((Screen.width, Screen.height))

# --- Configuración del Patrón Prototipo ---

# 1. Definimos los tipos de eventos base
base_flying_event = pygame.USEREVENT + 1
base_landscape_event = pygame.USEREVENT + 10

# 2. Creamos listas de prototipos
prototypes_flying = [Bird(), Umbrella(), Jet(), Missile()]
prototypes_landscape = [Cloud(), Mountain()]

# 3. Definimos los períodos (en ms) para cada prototipo
# Bird(400), Umbrella(500), Jet(1000), Missile(2500)
periods_flying = [400, 500, 1000, 2500]
# Cloud(500), Mountain(2000)
periods_landscape = [500, 3000]

# 4. Creamos las fábricas
factory_flying = FactorySprites(prototypes_flying, periods_flying, 
                                base_flying_event)
factory_landscape = FactorySprites(prototypes_landscape, periods_landscape, 
                                   base_landscape_event)

# 5. Instanciamos Game con las fábricas
game = Game(factory_flying, factory_landscape)

# play
game.play()