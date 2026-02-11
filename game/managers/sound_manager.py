from typing import Dict
from pathlib import Path
from pygame import mixer, mixer_music

from game.settings import GameSettings
from game.managers.asset_manager_error import AssetManagerError

class SoundManager:
    """Manager para efectos de sonido (SFX) y música de fondo (BGM).
    
    Diferencia entre mixer.Sound (memoria) y mixer_music (streaming).
    """

    def __init__(self) -> None:
        """Inicializa los directorios de audio y la caché de SFX."""
        self._sounds_dir: Path = GameSettings.SOUNDS_DIR
        self._music_dir: Path = GameSettings.MUSIC_DIR
        self._sfx_cache: Dict[str, mixer.Sound] = {}

    def play_sfx(self, name: str, volume: float = 1.0) -> None:
        """Reproduce un efecto de sonido corto.

        Args:
            name: Nombre del archivo .wav.
            volume: Nivel de volumen entre 0.0 y 1.0.
        """
        try:
            if name not in self._sfx_cache:
                path: Path = self._sounds_dir / f"{name}.mp3"
                self._sfx_cache[name] = mixer.Sound(path)
            
            sound = self._sfx_cache[name]
            sound.set_volume(volume)
            sound.play()
        except Exception as e:
            raise AssetManagerError(f"No se pudo reproducir el SFX {name}: {e}")

    def play_music(self, name: str, loops: int = -1, volume: float = 0.5) -> None:
        """Inicia el streaming de una pista de música.

        Args:
            name: Nombre del archivo .mp3.
            loops: Número de repeticiones (-1 para infinito).
            volume: Nivel de volumen.
        """
        path: Path = self._music_dir / f"{name}.mp3"
        try:
            mixer_music.load(str(path))
            mixer_music.set_volume(volume)
            mixer_music.play(loops)
        except Exception as e:
            raise AssetManagerError(f"No se pudo reproducir la música {name}: {e}")


    @staticmethod
    def stop_music() -> None:
        """Detiene la música actual."""
        mixer_music.stop()

    @staticmethod
    def pause_music() -> None:
        """Pausa la música actual."""
        mixer_music.pause()

    @staticmethod
    def resume_music() -> None:
        """Reanuda la música pausada."""
        mixer_music.unpause()