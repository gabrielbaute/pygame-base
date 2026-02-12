import logging
from typing import Dict
from pathlib import Path
from pygame import image, Surface

from game.settings import GameSettings
from game.managers.asset_manager_error import AssetManagerError

class ImageManager:
    """Clase para la gestión centralizada de superficies (imágenes).
    
    Implementa un sistema de caché para evitar cargas redundantes desde disco.
    """

    def __init__(self) -> None:
        """Inicializa el manager con el directorio configurado en GameSettings."""
        self.logger = logging.getLogger(self.__class__.__name__)
        self._images_dir: Path = GameSettings.IMG_DIR
        self._cache: Dict[str, Surface] = {}

    def get_image(self, name: str) -> Surface:
        """Obtiene una imagen, cargándola desde disco si no está en caché.

        Args:
            name: El nombre del archivo de imagen (sin extensión .png).

        Returns:
            La superficie de Pygame optimizada con convert_alpha().

        Raises:
            AssetManagerError: Si el archivo no existe o no se puede cargar.
        """
        if name not in self._cache:
            path: Path = self._images_dir / f"{name}.png"
            try:
                img: Surface = image.load(path).convert_alpha()
                self._cache[name] = img
            except Exception as e:
                self.logger.exception(f"No se pudo cargar la imagen {path}: {e}")
                raise AssetManagerError(f"No se pudo cargar la imagen {path}: {e}")
        
        return self._cache[name]

    def load_all(self) -> None:
            """Escanea el directorio de imágenes y las carga todas en memoria."""
            # Buscamos todos los archivos .png en el directorio
            files = list(self._images_dir.glob("*.png"))
            
            for file_path in files:
                name = file_path.stem  # stem obtiene el nombre sin extensión
                if name not in self._cache:
                    try:
                        self._cache[name] = image.load(file_path).convert_alpha()
                        self.logger.debug(f"Cargando imagen {file_path}")
                    except Exception as e:
                        self.logger.exception(f"No se pudo cargar la imagen {file_path}: {e}")
                        continue