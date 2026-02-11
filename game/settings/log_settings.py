import logging
from pathlib import Path
from typing import Dict, Optional

from game.settings.game_settings import GameSettings

class GameLogger:
    """
    Configuración del sistema de logs.
    """
    LOG_FILE: Path = GameSettings.LOGS_DIR / f"{GameSettings.GAME_NAME}.log"
    LEVEL_MAP: Dict[str, int] = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    @staticmethod
    def setup_logging(level: Optional[str] = "INFO") -> None:
        """
        Configura el sistema de logging básico.

        Args:
            level (Optional[str]): Nivel de registro. Ejemplo: "DEBUG", "INFO", etc.

        Returns:
            None
        """
        GameSettings.LOGS_DIR.mkdir(parents=True, exist_ok=True)

        if not GameLogger.LOG_FILE.exists():
            GameLogger.LOG_FILE.touch()
        
        logging.basicConfig(
            level=GameLogger.LEVEL_MAP.get(level, logging.INFO),
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                logging.FileHandler(GameLogger.LOG_FILE, encoding="utf-8"),
                logging.StreamHandler()
            ]
        )
