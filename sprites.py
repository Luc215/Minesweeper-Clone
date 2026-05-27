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
        if self.revealed and not self.flagged:
            boardSurface.blit(self.image, (self.x, self.y))
        elif not self.revealed and self.flagged:
            boardSurface.blit(tileFlag, (self.x, self.y))
        elif not self.revealed:
            boardSurface.blit(tileUnknown, (self.x, self.y))

    def __repr__(self):
        return self.type

class Board:
    def __init__(self):
        self.surface = pygame.Surface((width,height))
        self.boardList = [[Tile(col, row, tileEmpty, ".") for row in range(rows)] for col in range(cols)]
        self.placeMines()
        self.placeClues()
        self.dug = []

    def placeMines(self):
        for _ in range(amountOfMines):
            while True:
                x = random.randint(0, cols - 1)
                y = random.randint(0, rows - 1)
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

    def dig(self, x, y):
        self.dug.append((x,y))
        if(self.boardList[x][y]).type == "X": # Implement lazy initialization
            self.boardList[x][y].revealed = True
            self.boardList[x][y].image = tileExploded 
            return False
        
        elif self.boardList[x][y].type == "C":
            self.boardList[x][y].revealed = True
            return True
        
        self.boardList[x][y].revealed = True

        for row in range(max(0,x-1), min(rows-1, x+1)+1):
            for col in range(max(0,y-1), min(cols-1, y+1)+1):
                if (row, col) not in self.dug:
                    self.dig(row,col)
            
        return True
            
    def displayBoard(self):
        for i in self.boardList:
            print(i)
