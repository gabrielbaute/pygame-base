from pathlib import Path

___version___ = "0.0.0"

class GameSettings:
    # Informacion sobre el juego
    GAME_NAME: str = "Game"
    GAME_VERSION: str = ___version___
    
    # Informacion sobre la pantalla
    WIDTH: int = 800
    HEIGHT: int = 600
    FPS: int = 60
    
    # Directorios base
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    HOME_DIR: Path = Path.home() / f".{GAME_NAME.lower()}"
    
    # Directorios de data local
    LOGS_DIR: Path = HOME_DIR / "logs"
    DATA_DIR: Path = HOME_DIR / "data"
    SETTINGS_DIR: Path = HOME_DIR / "settings"
    RESOURCES_DIR: Path = HOME_DIR / "resources"
    
    # Directorios de assets
    ASSETS_DIR: Path = BASE_DIR / "assets"
    IMG_DIR: Path = ASSETS_DIR / "img"
    SOUNDS_DIR: Path = ASSETS_DIR / "sounds"
    MUSIC_DIR: Path = ASSETS_DIR / "music"
    
    @classmethod
    def initialize_directories(cls) -> None:
        """Crea la estructura de carpetas necesaria para el juego."""
        for directory in [cls.HOME_DIR, cls.LOGS_DIR, cls.DATA_DIR]:
            directory.mkdir(parents=True, exist_ok=True)
        
        for data_directory in [cls.SETTINGS_DIR, cls.RESOURCES_DIR]:
            data_directory.mkdir(parents=True, exist_ok=True)
