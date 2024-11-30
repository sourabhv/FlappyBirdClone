# import asyncio
#
# from src_old.flappy import Flappy
#
# if __name__ == "__main__":
#     asyncio.run(Flappy().start())


import src.game

if __name__ == "__main__":
    game = src.game.Game()
    game.main_loop()
