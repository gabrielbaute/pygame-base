from enum import Enum, auto

class GameState(Enum):
    """Tipificación de los estados globales del juego."""
    MENU = auto()
    PLAYING = auto()
    PAUSED = auto()
    GAME_OVER = auto()
    CREDITS = auto()
    EXIT = auto()