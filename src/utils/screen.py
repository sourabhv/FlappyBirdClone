class Screen:
    def __init__(self, screen):
        self.screen = screen

    def flush(self, sprites: list):
        for s in sprites:
            s.blit(self.screen)
