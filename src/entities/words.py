import pygame
from src.utils.manager import Manager
import random

class Words:
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.image_GM = Manager.get_instance().gameover
        self.rect_GM = pygame.Rect(48, 235, 192, 42)

        self.image_M = Manager.get_instance().message
        self.rect_M = pygame.Rect(52, 122.5, 184, 267)
    def draw_GM(self):
        self.display_surface.blit(self.image_GM, self.rect_GM)


    def draw_M(self):
        self.display_surface.blit(self.image_M, self.rect_M)



