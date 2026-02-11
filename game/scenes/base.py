from pygame import Surface
from pygame.event import Event
from abc import ABC, abstractmethod
from typing import List, Optional, TYPE_CHECKING

from game.enums import GameState

if TYPE_CHECKING:
    from game.managers.scene_manager import SceneManager

class Scene(ABC):
    """Interfaz abstracta para todas las escenas del juego."""
    
    def __init__(self) -> None:
        self.next_scene: 'Scene' = self  # Referencia a sí misma por defecto
        self.pending_state_change: Optional[GameState] = None

    def request_change(self, state: GameState) -> None:
        """Método para solicitar un cambio de estado global."""
        self.pending_state_change = state

    @abstractmethod
    def handle_events(self, events: List[Event]) -> None:
        """Procesa entradas de teclado/ratón."""
        pass

    @abstractmethod
    def update(self, dt: float) -> None:
        """Actualiza la lógica de la escena."""
        pass

    @abstractmethod
    def draw(self, screen: Surface) -> None:
        """Dibuja la escena en la pantalla."""
        pass

    def change_to(self, scene: 'Scene') -> None:
        """Prepara la transición a la siguiente escena."""
        self.next_scene = scene