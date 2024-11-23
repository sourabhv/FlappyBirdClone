import pygame.image
import os


FILE_ROOT = r"F:\projects\FlapPyBird\assets\sprites"


class Manager:
    # num0 = pygame.image.load(FILE_ROOT + "0.png")

    def __init__(self):
        self.assets_dictionary = {}
        for path, folders, files in os.walk(FILE_ROOT):
            print(files)
            for f in files:
                k = f.split(".")[0]
                self.assets_dictionary[k] = pygame.image.load(os.path.join(path, f))
                # print(self.assets_dictionary)

Manager()
