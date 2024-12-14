class Stats:  # FIXME: singleton mode implementation
    stat_list = ["welcome", "run", "gameover"]
    #WELCOME, RUN, GAMEOVER = range(3)
    def __init__(self):
        self.stat = self.stat_list[0]
        #self.stat = Stats.WELCOME
    def reset(self):
        self.stat = self.stat_list[0]
