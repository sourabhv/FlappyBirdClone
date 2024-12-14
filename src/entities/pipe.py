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

        self.x_0 = 200
        self.x_1 = self.x_0 + 170
        self.y_0 = random.randint(200, 380)
        self.y_1 = random.randint(200, 380)

        self.rect_0 = pygame.Rect(self.x_0, self.y_0, 52, 320)
        self.rect_1 = pygame.Rect(self.x_1, self.y_1, 52, 320)
        self.rect_2 = pygame.Rect(self.x_0, (self.y_0 - 500), 52, 320)
        self.rect_3 = pygame.Rect(self.x_1, (self.y_1 - 500), 52, 320)
        self.rect_list = [self.rect_0, self.rect_1]
        self.rect_list_all = [self.rect_0, self.rect_1, self.rect_2, self.rect_3]
    def update(self):
        self.x_0 -= 2
        self.x_1 -= 2
        self.rect_0 = pygame.Rect(self.x_0, self.y_0, 52, 320)
        self.rect_1 = pygame.Rect(self.x_1, self.y_1, 52, 320)
        self.rect_2 = pygame.Rect(self.x_0, (self.y_0 - 500), 52, 320)
        self.rect_3 = pygame.Rect(self.x_1, (self.y_1 - 500), 52, 320)
        self.rect_list_all = [self.rect_0, self.rect_1, self.rect_2, self.rect_3]
        self.rect_list = [self.rect_0, self.rect_1]
        if self.x_0 <= -52:
            self.x_0 = 288
            self.y_0 = random.randint(200, 380)
        if self.x_1 <= -52:
            self.x_1 = 288
            self.y_1 = random.randint(200, 380)


    def draw(self):
        for x in self.rect_list_all:
            if x in self.rect_list:
                self.display_surface.blit(self.image_up, x)
            else:
                self.display_surface.blit(self.image_down, x)

