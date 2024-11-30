from src.utils.manager import Manager
import random
# from src.utils.stats import Stats

class Background:
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.manager = Manager()
        self.image = self.manager.background[random.randint(0, 1)]

    def draw(self):
        self.display_surface.blit(self.image, self.image.get_rect())
