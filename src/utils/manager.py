import pygame.image
import os

FILE_ROOT = f"{os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))}/assets/sprites/"

class Manager:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((288, 512))


        red_bird_name = ["redbird-downflap", "redbird-midflap", "redbird-upflap"]
        yellow_bird_name = ["yellowbird-downflap", "yellowbird-midflap", "yellowbird-upflap"]
        blue_bird_name = ["bluebird-downflap", "bluebird-midflap", "bluebird-upflap"]
        background_name = ["background-day", "background-night"]
        pipe_name = ["pipe-green", "pipe-red"]

        blue_bird = [pygame.image.load(image.join([FILE_ROOT, ".png"])).convert_alpha()
                     for image in blue_bird_name]
        red_bird = [pygame.image.load(image.join([FILE_ROOT, ".png"])).convert_alpha()
                      for image in red_bird_name]
        yellow_bird = [pygame.image.load(image.join([FILE_ROOT, ".png"])).convert_alpha()
                         for image in yellow_bird_name]

        self.birds = [blue_bird, red_bird, yellow_bird]
        self.numbers = [pygame.image.load(image.join([FILE_ROOT, ".png"])).convert_alpha()
                         for image in [str(x) for x in range(10)]]
        self.background = [pygame.image.load(image.join([FILE_ROOT, ".png"])).convert_alpha()
                      for image in background_name]
        self.pipes = [pygame.image.load(image.join([FILE_ROOT, ".png"])).convert_alpha()
                      for image in pipe_name]
        self.base = pygame.image.load(os.path.join(FILE_ROOT, "base.png")).convert_alpha()
        self.gameover = pygame.image.load(os.path.join(FILE_ROOT, "gameover.png")).convert_alpha()
        self.message = pygame.image.load(os.path.join(FILE_ROOT, "message.png")).convert_alpha()

    @staticmethod
    def get_instance():
        return instance

instance = Manager()
