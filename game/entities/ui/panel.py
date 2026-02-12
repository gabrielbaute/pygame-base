import pygame
from game.entities.base import Entity
from game.settings.color_settings import ColorRGB, GameColors

class Panel(Entity):
    """
    Contenedor visual que puede servir de fondo para menús o interfaces.
    """
    def __init__(
        self, 
        width: int, 
        height: int, 
        position: tuple[int, int], 
        color: ColorRGB = GameColors.Gray.Black,
        alpha: int = 180,
        border_radius: int = 10
    ) -> None:
        # Creamos una superficie que soporte transparencia (SRCALPHA)
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        super().__init__(surface, *position)
        
        self.color = color
        self.alpha = alpha
        self.border_radius = border_radius
        self._render_panel()

    def _render_panel(self) -> None:
        """Dibuja el rectángulo con bordes redondeados y transparencia."""
        # Creamos el color con alpha
        rgba = (*self.color, self.alpha)
        pygame.draw.rect(
            self.image, 
            rgba, 
            self.image.get_rect(), 
            border_radius=self.border_radius
        )

    def update(self, dt: float) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)