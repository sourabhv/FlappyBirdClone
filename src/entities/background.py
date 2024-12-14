from src.utils.manager import Manager
from src.utils.stats import Stats
import pygame
import random

class Background:
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.stat = Stats().stat
        self.base_image = Manager.get_instance().base
        self.image = Manager.get_instance().background[random.randint(0, 1)]
        self.rect = pygame.Rect(0, 400, 336, 112)

    def draw(self):
        self.stat = Stats().stat
        #画背景
        self.display_surface.blit(self.image, self.image.get_rect())
        #画地面
        if self.stat in ["welcome", "gameover"]:
            self.display_surface.blit(self.base_image, self.rect)
        elif self.stat == "run":
            self.rect.move_ip(-5, 0)
            self.display_surface.blit(self.base_image, self.rect)
            self.display_surface.blit(self.base_image, self.rect.move(336, 0))
            if self.rect.x <= -336:
                self.rect.x = 0