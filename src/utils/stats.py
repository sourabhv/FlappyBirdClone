class Stats:  # FIXME: singleton mode implementation
    stat_list = ["welcome", "run", "gameover"]
    def __init__(self):
        self.stat = self.stat_list[1]
    def reset(self):
        self.stat = self.stat_list[0]
