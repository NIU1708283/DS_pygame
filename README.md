# Pygame Prototype

A small 2D Pygame game prototype in which the player pilots a helicopter through a continuously changing landscape. Flying objects are spawned at regular intervals, and the game ends when the helicopter collides with one of them.

The project started from the [Real Python Pygame primer](https://realpython.com/pygame-a-primer/) and was refactored around a dedicated `Game` class. It also demonstrates the Prototype and Factory patterns for creating game sprites.

## Requirements

- Python 3.8 or newer
- [Pygame](https://www.pygame.org/)

## Installation

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Install the dependency:

	```bash
	python -m pip install pygame
	```

## Running the game

Run the entry point from the project directory so that the image and audio paths resolve correctly:

```bash
python main.py
```

## Controls

| Key | Action |
| --- | --- |
| Arrow keys | Move the helicopter up, down, left, and right |
| `Escape` | Quit the game |
| Window close button | Quit the game |

The helicopter is kept inside the 800 x 600 game window. A collision with a flying object stops the game and plays the collision sound.

## Project structure

| File or directory | Purpose |
| --- | --- |
| `main.py` | Initializes Pygame, registers sprite prototypes, creates the factories, and starts the game |
| `game.py` | Main loop, event handling, sprite groups, drawing, collision detection, music, and sounds |
| `player.py` | Player helicopter movement, screen boundaries, and movement sounds |
| `game_sprite.py` | Abstract base class for cloneable game sprites |
| `factory_sprites.py` | Registers timers and creates sprite clones from prototypes |
| `bird.py`, `umbrella.py`, `jet.py`, `missile.py` | Flying sprites; these can collide with the player |
| `cloud.py`, `mountain.py` | Landscape sprites |
| `screen.py` | Window size constants |
| `icons/` | Sprite images |
| `sounds_music/` | Background music and sound effects |
| `pygame-prototype.puml` | PlantUML class diagram |

## Design overview

`main.py` creates prototype instances and supplies them to two `FactorySprites` objects:

- The flying factory spawns a bird, umbrella, jet, or missile.
- The landscape factory spawns clouds and mountains.

Each factory uses a Pygame timer for its prototypes. When a timer event reaches `Game`, the factory clones the matching prototype and adds the new sprite to the appropriate sprite groups. The game loop then updates and draws all active sprites at approximately 30 FPS.

## Credits

- Initial project inspiration: [Real Python Pygame primer](https://realpython.com/pygame-a-primer/)
- Original tutorial materials: [realpython/materials](https://github.com/realpython/materials/tree/master/pygame-a-primer)
- Game artwork: [OpenGameArt](https://opengameart.org)
