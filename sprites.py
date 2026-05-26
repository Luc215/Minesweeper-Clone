from settings import *

'''
'.' : Unknown tile
'X' : Exploded Tile
'C' : Clue
'/' : Empty
'''
class Tile:
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        self.x, self.y = x * tileSize, y * tileSize
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged

    def __repr__(self):
        return self.type

class Board:
    def __init__(self):
        self.surface = pygame.Surface((width,height))
        self.boardList = [[Tile(col, row, tileEmpty, ".") for row in range(rows)] for col in range(cols)]

    def displayBoard(self):
        for i in self.boardList:
            print(i)
