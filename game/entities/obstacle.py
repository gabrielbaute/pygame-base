from pygame import Surface

from game.entities.base import Entity

class Obstacle(Entity):
    """Un obstáculo estático que no requiere motor de física."""
    def __init__(self, image: Surface, x: float, y: float) -> None:
        super().__init__(image)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, dt: float) -> None:
        # Los obstáculos estáticos no suelen necesitar lógica de frame
        pass

    def draw(self, screen: Surface) -> None:
        screen.blit(self.image, self.rect)