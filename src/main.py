import sys

import pygame

from src.utils.screen import Screen
from src.utils.settings import Settings


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.settings = Settings()
        self.screen = Screen(pygame.display.set_mode(self.settings.window_size))
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

    def main_loop(self):
        while True:
            self.handle_events()
            pygame.display.flip()
            self.clock.tick(self.settings.fps)


    def initialize(self):
        pass
