from random import shuffle

class Movement:
    
    def __init__(self, movements, shfl=False):
        # shuffle(movements)
        self.movements = movements
        self.selected = 0
        self.shuffle = shfl

    def getMovement(self):
        mvmnt = self.movements[self.selected]
        self.selected += 1

        if self.selected == len(self.movements):
            self.selected = 0
            if self.shuffle:
                shuffle(self.movements)
        
        return mvmnt