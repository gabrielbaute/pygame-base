from abc import ABC, abstractmethod
from typing import Optional
from pygame import Surface

from game.core import PhysicsBody

class Entity(ABC):
    """Clase base abstracta para todos los objetos del juego."""
    
    def __init__(self, image: Surface) -> None:
        self.image = image
        # Opcional: no todas las entidades tienen física
        self.physics: Optional[PhysicsBody] = None

    @abstractmethod
    def update(self, dt: float) -> None:
        """Contrato para la lógica de actualización."""
        pass

    @abstractmethod
    def draw(self, screen: Surface) -> None:
        """Contrato para el renderizado."""
        pass