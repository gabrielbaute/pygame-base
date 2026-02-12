from pygame import draw, Rect, Surface

from game.entities.base import Entity
from game.settings import ColorRGB, GameColors


class ProgressBar(Entity):
    """
    Barra de progreso para representar recursos (Vida, Energía, Carga).
    """
    def __init__(
        self,
        width: int,
        height: int,
        position: tuple[int, int],
        bar_color: ColorRGB = GameColors.Green.Green,
        bg_color: ColorRGB = GameColors.Gray.DarkGray,
        border_color: ColorRGB = GameColors.Gray.Black
    ) -> None:
        surface = Surface((width, height))
        super().__init__(surface, *position)
        
        self.bar_color = bar_color
        self.bg_color = bg_color
        self.border_color = border_color
        
        self.progress: float = 1.0  # Rango 0.0 a 1.0
        self._border_width = 2

    def set_progress(self, current: float, maximum: float) -> None:
        """Actualiza el valor de la barra asegurando que esté en el rango [0, 1]."""
        if maximum <= 0:
            self.progress = 0
        else:
            self.progress = max(0.0, min(1.0, current / maximum))

    def update(self, dt: float) -> None:
        # Aquí podrías añadir interpolación para que la barra 
        # baje suavemente en lugar de saltar instantáneamente.
        pass

    def draw(self, screen: Surface) -> None:
        # 1. Dibujar fondo
        draw.rect(screen, self.bg_color, self.rect)
        
        # 2. Calcular y dibujar la barra de progreso (el relleno)
        inner_width = int((self.rect.width - (self._border_width * 2)) * self.progress)
        if inner_width > 0:
            fill_rect = Rect(
                self.rect.x + self._border_width,
                self.rect.y + self._border_width,
                inner_width,
                self.rect.height - (self._border_width * 2)
            )
            draw.rect(screen, self.bar_color, fill_rect)
        
        # 3. Dibujar borde
        draw.rect(screen, self.border_color, self.rect, self._border_width)