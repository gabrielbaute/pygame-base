import pygame
from typing import List
from pygame.event import Event
from pygame import Surface

from game.scenes.base import Scene
from game.settings.color_settings import GameColors
from game.settings.game_settings import GameSettings

class MenuScene(Scene):
    """Escena del menú principal."""

    def __init__(self) -> None:
        super().__init__()
        # Aquí podrías usar tu ImageManager para cargar un logo
        # self.logo = image_manager.get_image("logo")
        self.font = pygame.font.SysFont("Arial", 48)
        self.title_surf = self.font.render(
            f"BIENVENIDO A {GameSettings.GAME_NAME}", 
            True, 
            GameColors.Gray.Black
        )
        self.title_rect = self.title_surf.get_rect(
            center=(GameSettings.WIDTH // 2, GameSettings.HEIGHT // 2)
        )

    def handle_events(self, events: List[Event]) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Transición lógica: aquí instanciarías la siguiente escena
                    # self.change_to(LevelOneScene())
                    print("Cambiando a LevelOneScene...")

    def update(self, dt: float) -> None:
        # Lógica de animaciones del menú (ej: un texto que parpadea)
        pass

    def draw(self, screen: Surface) -> None:
        screen.fill(GameColors.White.GhostWhite)
        screen.blit(self.title_surf, self.title_rect)