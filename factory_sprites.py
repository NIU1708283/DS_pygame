import pygame


class FactorySprites:
    def __init__(self, prototypes: list, periods: list, base_event_type: int):
        self._prototypes = {}
        self.event_types = []

        # Configurar un temporizador y un tipo de evento para cada prototipo
        for i, prototype in enumerate(prototypes):
            event_type = base_event_type + i
            period = periods[i]

            # Añadir el evento al temporizador de Pygame
            pygame.time.set_timer(event_type, period)

            # Guardar el prototipo asociado a su tipo de evento
            self._prototypes[event_type] = prototype
            self.event_types.append(event_type)

    def make(self, event_type: int):
        """
        Crea un nuevo sprite clonando el prototipo
        asociado al tipo de evento dado.
        """
        if event_type not in self.event_types:
            return None

        prototype = self._prototypes[event_type]
        return prototype.clone()
        """
        return self._prototypes[event_type - self.event_types[0]].clone()
        # esto no sirve
        """