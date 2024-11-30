import pygame
import random
import sys

class Bird(object):
    def __init__(self):
                # 定义一个小鸟类
        self.birdRect = pygame.Rect(65, 50, 50, 50)
        self.birdStatus = [[pygame.image.load(r"C:\Users\dell\PycharmProjects\FlapPyBird\assets\sprites\bluebird-downflap.png"),pygame.image.load(r"C:\Users\dell\PycharmProjects\FlapPyBird\assets\sprites\bluebird-midflap.png"),pygame.image.load(r"C:\Users\dell\PycharmProjects\FlapPyBird\assets\sprites\bluebird-upflap.png")],
                           [pygame.image.load(r"C:\Users\dell\PycharmProjects\FlapPyBird\assets\sprites\redbird-downflap.png"),pygame.image.load(r"C:\Users\dell\PycharmProjects\FlapPyBird\assets\sprites\redbird-midflap.png"),pygame.image.load(r"C:\Users\dell\PycharmProjects\FlapPyBird\assets\sprites\redbird-upflap.png")],
                           [pygame.image.load(r"C:\Users\dell\PycharmProjects\FlapPyBird\assets\sprites\yellowbird-downflap.png"),pygame.image.load(r"C:\Users\dell\PycharmProjects\FlapPyBird\assets\sprites\yellowbird-midflap.png"),pygame.image.load(r"C:\Users\dell\PycharmProjects\FlapPyBird\assets\sprites\yellowbird-upflap.png")]]
        self.status = 0
        self.birdx = 5
        self.birdy = 350
        self.jump = False
        self.jumpSpeed = 10
        self.gravity = 5
        self.dead = False

    def birdUpdate(self):  # 定义移动方法
        if self.jump:
         # 小鸟跳跃状态
            self.jumpSpeed -= 1
            self.birdy = self.birdy - self.jumpSpeed
        else:
            self.gravity += 0.2
            self.birdy = self.birdy + self.gravity
            self.birdRect[1] = self.birdy

def createMap():

    colorBird=random.choice(0,3)
    if not Bird.dead:
        Screen.blit(Bird.birdStatus[colorBird][0], (Bird.birdx, Bird.birdy))
        Bird.birdUpdate()
        pygame.display.update()
        Screen.blit(Bird.birdStatus[colorBird][1], (Bird.birdx, Bird.birdy))
        Bird.birdUpdate()
        pygame.display.update()
        Screen.blit(Bird.birdStatus[colorBird][2], (Bird.birdx, Bird.birdy))
        Bird.birdUpdate()
        pygame.display.update()


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not Bird.dead:
            Bird.jump = True
            Bird.jumpSpeed = 15
            Bird.gravity = 3

    if not checkDead():
        createMap()


def checkDead():
    #检测小鸟是否死亡

    upRect=pygame.Rect(Pipeline.wallx,-150,Pipeline.pineUp.get_width(),Pipeline.pineUp.get_height())
    downRect = pygame.Rect(Pipeline.wallx, 400, Pipeline.pineDown.get_width(), Pipeline.pineDown.get_height())
    #检测矩形碰撞
    if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
        Bird.dead=True
    #边界检测
    if not 0<Bird.birdRect[1] <height:
        Bird.dead = True
        return True
    else :
        return False



