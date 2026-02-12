import logging
from pathlib import Path
from pygame import Surface
from pygame.font import Font, SysFont
from typing import Dict, Tuple, Optional, TYPE_CHECKING

from game.settings import GameSettings

if TYPE_CHECKING:
    from game.settings.color_settings import ColorRGB

class FontManager:
    """
    Gestor para la carga y caché de fuentes tipográficas.
    Evita la carga redundante de archivos TTF desde el disco.
    """
    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self._fonts: Dict[Tuple[str, int], Font] = {}
        self._default_font_path: Optional[Path] = GameSettings.FONTS_DIR/ "RubikIso-Regular.ttf"

    def get_font(self, size: int, name: Optional[str] = None) -> Font:
        """
        Obtiene una fuente de la caché o la carga si no existe.

        Args:
            size: Tamaño de la fuente.
            name: Nombre del archivo de fuente (opcional). Si es None, usa la default.

        Returns:
            El objeto Font listo para usar.
        """
        key = (name if name else "default", size)
        
        if key not in self._fonts:
            try:
                path: Path = GameSettings.FONTS_DIR / f"{name}.ttf" if name else self._default_font_path
                # Si el path no existe, Pygame usa una fuente por defecto del sistema
                self._fonts[key] = Font(str(path), size)
            except Exception as e:
                self.logger.exception(f"No se pudo cargar la fuente {key}: {e}")
                self.logger.warning("Cargando fuente por defecto. Usando fuente por defecto.")
                self._fonts[key] = SysFont("Arial", size)
        
        return self._fonts[key]

    def render(
            self, 
            text: str, 
            size: int, 
            color: ColorRGB, 
            name: Optional[str] = None, 
            antialias: bool = True
        ) -> Surface:
        """
        Método de conveniencia para obtener directamente la Surface del texto.

        Args:
            text: El texto a renderizar.
            size: Tamaño de la fuente.
            color: Tupla RGB para el color del texto.
            name: Nombre del archivo de fuente (opcional
            antialias: 
        """
        font = self.get_font(size, name)
        return font.render(text, antialias, color)