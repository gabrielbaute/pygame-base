from abc import ABC, abstractmethod
from typing import Optional
from pygame import Surface, Rect

from game.core import PhysicsBody

class Entity(ABC):
    """Clase base abstracta para todos los objetos del juego."""
    
    def __init__(self, image: Surface, x: float = 0, y: float = 0) -> None:
        self.image: Surface = image
        self.rect: Rect = self.image.get_rect(topleft=(x, y))
        self.physics: Optional[PhysicsBody] = None

    @abstractmethod
    def update(self, dt: float) -> None:
        """Contrato para la lógica de actualización."""
        pass

    @abstractmethod
    def draw(self, screen: Surface) -> None:
        """Contrato para el renderizado."""
        screen.blit(self.image, self.rect)