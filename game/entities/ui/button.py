from typing import Callable
from pygame import Surface, mouse

from game.managers import FontManager
from game.entities.base import Entity
from game.entities.ui.label import Label
from game.settings import ColorRGB, GameColors

class Button(Entity):
    def __init__(
        self,
        font_manager: FontManager,
        text: str,
        position: tuple[int, int],
        callback: Callable[[], None],
        base_color: ColorRGB = GameColors.Gray.DimGray,
        hover_color: ColorRGB = GameColors.Gray.Silver
    ) -> None:
        self.font_manager = font_manager
        self.callback = callback
        self.colors = {"base": base_color, "hover": hover_color}
        self.is_hovered = False
        
        # Creamos el Label interno para el texto
        self.label = Label(font_manager, text, size=32, color=GameColors.White.White)
        
        # El botón en sí es una superficie que envuelve al texto con un margen
        button_surf = Surface((self.label.rect.width + 20, self.label.rect.height + 10))
        super().__init__(button_surf, *position)
        
        self.label.rect.center = self.rect.center # Centramos texto en botón

    def update(self, dt: float) -> None:
        """
        Actualiza el estado del botón.
        """
        mouse_pos = mouse.get_pos()
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        
        # Si hay clic izquierdo
        if self.is_hovered and mouse.get_pressed()[0]:
            self.callback()

    def draw(self, screen: Surface) -> None:
        """
        Dibuja el botón en la pantalla.

        Args:
            screen (Surface): La superficie en la que se dibujará el botón.
        """
        # Cambiamos color según hover
        current_color = self.colors["hover"] if self.is_hovered else self.colors["base"]
        self.image.fill(current_color)
        
        # Dibujamos el fondo del botón y luego el label
        screen.blit(self.image, self.rect)
        self.label.draw(screen)