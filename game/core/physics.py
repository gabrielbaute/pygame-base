from pygame.math import Vector2
from game.core.physics_body import PhysicsBody

class PhysicsEngine:
    """Motor encargado de aplicar las leyes de la cinemática."""
    
    def __init__(self, gravity: float = 9.8) -> None:
        self.gravity: Vector2 = Vector2(0, gravity)
        self._entities: list = []

    def add_entity(self, entity: any) -> None:
        """Registra una entidad que tenga un atributo 'physics'."""
        if hasattr(entity, 'physics'):
            self._entities.append(entity)

    def update(self, dt: float) -> None:
        """Actualiza la física de todas las entidades.
        
        Args:
            dt: Delta Time (tiempo transcurrido desde el último frame).
        """
        for entity in self._entities:
            pb: PhysicsBody = entity.physics
            
            # 1. Aplicar Gravedad
            force_gravity = self.gravity * pb.gravity_scale
            pb.acceleration += force_gravity
            
            # 2. Actualizar Velocidad (v = v0 + a * dt)
            pb.velocity += pb.acceleration * dt
            pb.velocity *= pb.friction  # Aplicar amortiguación
            
            # 3. Actualizar Posición (s = s0 + v * dt)
            pb.position += pb.velocity * dt
            
            # 4. Limpiar aceleración para el siguiente frame
            pb.acceleration *= 0