import sys

import pygame

#from src.utils.screen import Screen
from src.utils.settings import Settings
from src.utils.manager import Manager
from src.entities.background import Background
from src.entities.words import Words


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.window_size)#改成Screen（）
        self.clock = pygame.time.Clock()
        self.manager = Manager()

        self.background = Background(self.screen)
        self.words = Words(self.background.image)

        self.stats = 0  #0=welcome,1=run,2=gameover

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #响应鼠标点击
                pass

    def update_screen(self):
        self.background.draw()

        pygame.display.flip()
        if self.stats == 0:
            self.words.draw_M()
            pass
            #画开始界面
        elif self.stats == 1:
            pass
            # 画游戏界面的物品
        elif self.stats == 2:
            self.words.draw_GM()

            pass
            #画gameover


    def main_loop(self):
        while True:
            self.handle_events()
            self.update_screen()

            self.clock.tick(self.settings.fps)




    def initialize(self):
        pass
