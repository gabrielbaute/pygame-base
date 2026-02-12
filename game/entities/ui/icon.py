import pygame
from game.entities.base import Entity

class Icon(Entity):
    """
    Representación visual simple de un asset de imagen para la UI.
    """
    def __init__(
        self, 
        image: pygame.Surface, 
        position: tuple[int, int],
        scale: float = 1.0
    ) -> None:
        if scale != 1.0:
            w, h = image.get_size()
            image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
        
        super().__init__(image, *position)

    def update(self, dt: float) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)