from typing import Dict, Optional

from game.scenes import Scene
from game.enums import GameState

class SceneManager:
    """
    Controlador central para la transición y gestión de escenas.
    """
    def __init__(self) -> None:
        self._scenes: Dict[GameState, Scene] = {}
        self._current_state: Optional[GameState] = None
        self._active_scene: Optional[Scene] = None

    def add_scene(self, state: GameState, scene: Scene) -> None:
        """
        Registra una escena asociada a un estado.

        Args:
            state (GameState): El estado al que se asocia la escena.
            scene (Scene): La escena a registrar.
        """
        self._scenes[state] = scene

    def set_state(self, new_state: GameState) -> None:
        """
        Cambia el estado actual y actualiza la escena activa.
        
        Args:
            new_state (GameState): El nuevo estado al que se cambiará.

        Raises:
            ValueError: Si el nuevo estado no tiene una escena asociada.
        """
        if new_state in self._scenes:
            self._current_state = new_state
            self._active_scene = self._scenes[new_state]
            # Podrías disparar logs aquí usando tu GameLogger
        else:
            raise ValueError(f"El estado {new_state} no tiene una escena asignada.")

    @property
    def active_scene(self) -> Scene:
        """Retorna la escena que debe ser procesada por el GameEngine."""
        if not self._active_scene:
            raise RuntimeError("No hay una escena activa configurada.")
        return self._active_scene