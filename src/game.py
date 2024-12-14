import sys
import pygame

#from src.utils.screen import Screen
from src.utils.settings import Settings
from src.utils.manager import Manager
from src.entities.background import Background
from src.entities.words import Words
from src.entities.pipe import Pipe
from src.entities.bird import Bird
from src.utils.stats import Stats


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.window_size)#改成Screen（）
        self.clock = pygame.time.Clock()
        self.manager = Manager()
        self.stats = Stats()

        self.stat = self.stats.stat

        self.background = Background(self.screen)
        self.words = Words(self.screen)
        self.pipe = Pipe(self.screen)
        self.bird = Bird(self.screen, self.pipe.rect_list_all)
        #self.stats = "gameover"  #0=welcome,1=run,2=gameover

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
                if not self.bird.dead:
                    self.stat = "run"
                self.bird.jump = True
                self.bird.jumpSpeed = -1
                print('mouse test')

    def update_screen(self):
        self.background.draw()

        if self.stat == "welcome":
            self.words.draw_M()

            #画开始界面
        elif self.stat == "run":
            self.pipe.draw()
            self.pipe.update()
            self.bird.birdUpdate()
            self.bird.createMap()
            self.bird.checkDead(self.pipe.rect_list_all)
            # 画游戏界面的物品
        elif self.stat == "gameover":
            self.pipe.draw()
            self.bird.createMap()
            self.words.draw_GM()

            #画gameover
        pygame.display.flip()


    def main_loop(self):
        while True:

            self.handle_events()
            self.update_screen()
            if self.bird.dead:
                self.stat = "gameover"


            self.clock.tick(self.settings.fps)




    def initialize(self):
        pass
