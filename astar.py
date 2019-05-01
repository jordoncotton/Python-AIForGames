# trying to implement 8 puzzle problem using A star algorithm
# The goal is: 0 1 2 3 4 5 6 7 8 and the heuristic used is 
# Manhattan distance. 

def __init__(self, starting, parent):
    self.board = starting
    self.parent = parent
    self.f = 0
    self.g = 0
    self.h = 0

def Manhattan(self):
    h = 0
    for i in range(3):
        for j in range(3):
                x, y = divmod(self.board[i][j], 3)
                h += abs(x - 1) + abs(y - j)
        return h
