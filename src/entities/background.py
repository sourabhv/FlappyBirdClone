from src.utils.manager import Manager
import pygame

class Background:
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.manager = Manager()
        self.image = pygame.image.load(r"F:\projects\FlapPyBird\assets\sprites\background-day.png").convert()
        self.rect = self.image.get_rect()
    def draw(self):
        self.display_surface.blit(self.image, self.rect)