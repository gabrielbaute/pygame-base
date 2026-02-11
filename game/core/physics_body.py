from dataclasses import dataclass
from pygame.math import Vector2

@dataclass
class PhysicsBody:
    """Representa las propiedades físicas de cualquier objeto en el juego."""
    position: Vector2
    velocity: Vector2
    acceleration: Vector2
    mass: float = 1.0
    friction: float = 0.98  # Resistencia del aire/suelo
    gravity_scale: float = 1.0  # Escala de la gravedad