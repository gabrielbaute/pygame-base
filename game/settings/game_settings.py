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
    
    # Musica
    FILE_MUSIC = "musica.mp3"
    
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
    
    DIRS = [HOME_DIR, LOGS_DIR, DATA_DIR, SETTINGS_DIR, RESOURCES_DIR, ASSETS_DIR, IMG_DIR, SOUNDS_DIR, MUSIC_DIR]
    for d in DIRS:
        d.mkdir(exist_ok=True)