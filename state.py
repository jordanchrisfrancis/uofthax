
class User:
    def __init__(self):
        self.levels = [0,0,0,0] # level for each stage
        self.scores = [0,0,0,0] # score for each stage
        self.cost = [50,100,150] # cost to upgrade from each level (level 0 -> level 1 is 50)
        self.state = 0 # state for current alcohol
        self.final_score = 0 # final score for alcohol
        self.tier = ' ' # tier assigned to alcohol
        self.money = 0 # amount of money collected
    
    def next_stage(self, score):
        if self.state == 3:
            self.scores[self.state] = score
            self.compute_score()
            self.scores = [0,0,0,0]
            self.state = 0
            self.final_score = 0
            self.tier = ' '
        else:
            self.scores[self.state] = score
            self.state +=1
    
    def compute_score(self):
        pass

    def upgrade(self, selected):
        if self.money >= self.cost[self.levels[selected]]:
            self.money -= self.cost[self.levels[selected]]
            self.levels[selected] += 1
        else:
            return -1
    
    def sold(self, money):
        self.money += money