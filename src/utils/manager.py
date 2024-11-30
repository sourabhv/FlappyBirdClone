import pygame.image
import os

FILE_ROOT = f"{os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))}/assets/sprites/"

class Manager:
    # num0 = pygame.image.load(FILE_ROOT + "0.png")

    def __init__(self):
        pygame.init()
        pygame.display.set_mode((288, 512))

        blue_bird_name = ["bluebird-downflap", "bluebird-midflap", "bluebird-upflap"]
        background_name = ["background-day", "background-night"]

        self.blue_bird = [pygame.image.load(image.join([FILE_ROOT, ".png"])).convert_alpha()
                     for image in blue_bird_name]

        self.background = [pygame.image.load(image.join([FILE_ROOT, ".png"])).convert_alpha()
                      for image in background_name]

        self.gameover = pygame.image.load(os.path.join(FILE_ROOT, "gameover.png")).convert_alpha()
        self.message = pygame.image.load(os.path.join(FILE_ROOT, "message.png")).convert_alpha()





        # self.assets_dictionary = {}
        # for path, folders, files in os.walk(FILE_ROOT):
        #     print(files)
        #     for f in files:
        #         k = f.split(".")[0]
        #         self.assets_dictionary[k] = pygame.image.load(os.path.join(path, f))
        #         # print(self.assets_dictionary)

Manager()
