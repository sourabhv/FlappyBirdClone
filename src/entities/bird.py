import pygame
import random
from src.utils.manager import Manager
from src.utils.stats import Stats

class Bird(object):
    def __init__(self, display_surface, rect):
                # 定义一个小鸟类
        self.rect_list = rect
        self.display_surface = display_surface
        self.birdRect = pygame.Rect(65, 50, 32, 24)
        self.birdStatus = Manager.get_instance().birds
        self.stat = Stats()
        self.birdx = 5
        self.birdy = 350
        self.jump = False
        self.jumpSpeed = 0
        self.gravity = 0.05
        self.dead = False
        self.colorBird=random.randint(0,2)
        self.v = 0

    def birdUpdate(self):
        # 定义移动方法
        self.v += self.gravity
        self.birdy += self.v
        self.birdy += self.jumpSpeed
        if self.jump:
        # 小鸟跳跃状态
            self.jumpSpeed += 0.15
            self.v = -2.5
            self.v += self.jumpSpeed

            if self.jumpSpeed >= 0:
                self.jumpSpeed = 0
                self.jump = False

    def createMap(self):
        self.birdRect = pygame.Rect(self.birdx, self.birdy, 32, 24)
        self.display_surface.blit(self.birdStatus[self.colorBird][0], self.birdRect)
        self.display_surface.blit(self.birdStatus[self.colorBird][1], self.birdRect)
        self.display_surface.blit(self.birdStatus[self.colorBird][2], self.birdRect)
        if not self.dead:
            self.birdUpdate()


    def checkDead(self, rect):
        #检测小鸟是否死亡
        self.rect_list = rect

        if 0 <= self.birdy <= 512:
            self.dead = False
            for x in self.rect_list:
                if x.colliderect(self.birdRect):
                    self.dead = True
                    print('1')

        else:
            self.dead = True

