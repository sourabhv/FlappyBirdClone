import pygame
import random
from src.utils.stats import Stats
from src.utils.manager import Manager

#pipe_length = 320
class Pipe:
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.images_list = Manager.get_instance().pipes
        self.image_up = self.images_list[random.randint(0, 1)]
        self.image_down = pygame.transform.flip(self.image_up, False, True)
        self.rect = pygame.Rect(100, 300, 52, 320)


    def draw(self):
        self.display_surface.blit(self.image_up, self.rect)
        #self.display_surface.blit(self.image_down, self.rect.move(0, -(320 + random.randint(80,300))))

# class Pipes(Pipe):
#     super().__init__()
#

