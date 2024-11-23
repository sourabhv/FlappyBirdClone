import sys

import pygame

#from src.utils.screen import Screen
from src.utils.settings import Settings
from src.utils.manager import Manager
from src.entities.background import Background


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.window_size)#改成Screen（）
        self.clock = pygame.time.Clock()
        self.manager = Manager()

        self.background = Background(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

    def draw_background(self):
        self.background.draw()


    def main_loop(self):
        while True:
            self.handle_events()
            self.draw_background()
            self.clock.tick(self.settings.fps)

            pygame.display.flip()


    def initialize(self):
        pass
