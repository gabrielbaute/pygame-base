from typing import Optional
from pygame import Surface

from game.managers import FontManager
from game.entities.base import Entity
from game.settings import ColorRGB, GameColors

class Label(Entity):
    """
    Elemento de UI para renderizar texto de forma eficiente.
    """
    def __init__(
        self, 
        font_manager: FontManager,
        text: str, 
        size: int, 
        color: ColorRGB = GameColors.Gray.Black,
        position: tuple[float, float] = (0, 0),
        font_name: Optional[str] = None
    ) -> None:
        # Inicializamos la clase base (Entity) sin imagen, la generaremos ahora
        super().__init__(image=Surface((0, 0))) 
        
        self.font_manager = font_manager
        self._text = text
        self._size = size
        self._color = color
        self._font_name = font_name
        self.position = position
        
        # Renderizado inicial
        self._render_text()

    def _render_text(self) -> None:
        """Genera la Surface de texto usando el manager."""
        self.image = self.font_manager.render(
            self._text, self._size, self._color, self._font_name
        )
        self.rect = self.image.get_rect(topleft=self.position)

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        if self._text != value:
            self._text = value
            self._render_text()  # Re-renderizamos solo si el texto cambia

    def update(self, dt: float) -> None:
        """Lógica opcional, como parpadeo o movimiento suave."""
        pass

    def draw(self, screen: Surface) -> None:
        """Dibuja el texto en la pantalla."""
        screen.blit(self.image, self.rect)