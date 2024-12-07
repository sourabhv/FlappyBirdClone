import pygame
import random
from src.utils.manager import Manager
import sys

class Bird(object):
    def __init__(self, display_surface):
                # 定义一个小鸟类
        self.display_surface = display_surface
        self.birdRect = pygame.Rect(65, 50, 50, 50)
        self.birdStatus = Manager.get_instance().birds
        self.clock = pygame.time.Clock()
        self.clock.tick(30)
        self.status = 0
        self.birdx = 5
        self.birdy = 350
        self.jump = False
        self.jumpSpeed = 10
        self.gravity = 0.1
        self.dead = False
        self.colorBird=random.randint(0,2)

    def birdUpdate(self):

        # 定义移动方法
        if self.jump:
         # 小鸟跳跃状态
            self.jumpSpeed -= 1
            self.birdy = self.birdy - self.jumpSpeed
        else:
            self.gravity += 0.1
            self.birdy = self.birdy + self.gravity
            self.birdRect[1] = self.birdy

    def createMap(self):
        if not self.dead:
            self.display_surface.blit(self.birdStatus[self.colorBird][0], (self.birdx, self.birdy))
            self.birdUpdate()
            self.display_surface.blit(self.birdStatus[self.colorBird][1], (self.birdx, self.birdy))
            self.birdUpdate()
            self.display_surface.blit(self.birdStatus[self.colorBird][2], (self.birdx, self.birdy))
            self.birdUpdate()



        for event in pygame.event.get():
            print(event for event in pygame.event.get())
            if event.type == pygame.MOUSEBUTTONDOWN and not self.dead:
                self.jump = True
                self.jumpSpeed = 15
                self.gravity = 3
                print('1')

        # if not checkDead():
        #self.createMap()


# def checkDead():
#     #检测小鸟是否死亡
#
#     upRect=pygame.Rect(Pipeline.wallx,-150,Pipeline.pineUp.get_width(),Pipeline.pineUp.get_height())
#     downRect = pygame.Rect(Pipeline.wallx, 400, Pipeline.pineDown.get_width(), Pipeline.pineDown.get_height())
#     #检测矩形碰撞
#     if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
#         Bird.dead=True
#     #边界检测
#     if not 0<Bird.birdRect[1] <height:
#         Bird.dead = True
#         return True
#     else :
#         return False



