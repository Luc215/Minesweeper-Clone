from settings import *
import random
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

    def draw(self, boardSurface):
        boardSurface.blit(self.image, (self.x, self.y))

    def __repr__(self):
        return self.type

class Board:
    def __init__(self):
        self.surface = pygame.Surface((width,height))
        self.boardList = [[Tile(col, row, tileEmpty, ".") for col in range(cols)] for row in range(rows)]
        self.placeMines()
        self.placeClues()

    def placeMines(self):
        for _ in range(amountOfMines):
            while True:
                x = random.randint(0, rows - 1)
                y = random.randint(0, cols - 1)
                if self.boardList[x][y].type != "X":
                    self.boardList[x][y].image = tileMine
                    self.boardList[x][y].type = "X"
                    break

    def placeClues(self):
        for x in range(rows):
            for y in range(cols):
                if self.boardList[x][y].type != "X":
                    totalMines = self.checkNeighbors(x,y)
                    if totalMines > 0:
                        self.boardList[x][y].image = tileNumbers[totalMines-1]
                        self.boardList[x][y].type = "C"

    @staticmethod
    def isInside(x, y):
        return 0 <= x < cols and 0 <= y < rows

    def checkNeighbors(self, x, y):
        totalMines = 0
        for xOffset in range (-1,2):
            for yOffset in range(-1,2):
                neighbourX = x + xOffset
                neighbourY = y + yOffset
                if self.isInside(neighbourX, neighbourY) and self.boardList[neighbourX][neighbourY].type == "X":
                    totalMines += 1
        return totalMines

    def draw(self, screen):
        for row in self.boardList:
            for tile in row:
                tile.draw(self.surface)
            screen.blit(self.surface, (0,0))
            
    def displayBoard(self):
        for i in self.boardList:
            print(i)
