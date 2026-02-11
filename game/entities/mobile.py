from pygame import Surface

from game.core import PhysicsBody
from game.entities.base import Entity

class MobileEntity(Entity):
    """Entidad que sí posee un cuerpo físico y es procesada por PhysicsEngine."""
    def __init__(self, image: Surface, physics_body: PhysicsBody) -> None:
        super().__init__(image)
        self.physics = physics_body

    def update(self, dt: float) -> None:
        # Aquí va lógica adicional (IA, inputs), 
        # pero la posición ya la cambió el PhysicsEngine antes de llegar aquí.
        pass

    def draw(self, screen: Surface) -> None:
        if self.physics:
            # Dibujamos en la posición que dicta la física
            screen.blit(self.image, (self.physics.position.x, self.physics.position.y))