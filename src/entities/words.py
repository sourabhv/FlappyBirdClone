import pygame
class Words:
    def __init__(self, display_surface):
        self.display_surface = display_surface

        self.image_GM = pygame.image.load(r"F:\projects\FlapPyBird\assets\sprites\gameover.png").convert().convert_alpha()
        self.rect_GM = pygame.Rect(48, 235, 192, 42)

        self.image_M = pygame.image.load(r"F:\projects\FlapPyBird\assets\sprites\message.png").convert().convert_alpha()
        self.rect_M = pygame.Rect(52, 122.5, 184, 267)
    def draw_GM(self):
        self.display_surface.blit(self.image_GM, self.rect_GM)


    def draw_M(self):
        self.display_surface.blit(self.image_M, self.rect_M)



