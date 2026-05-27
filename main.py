import sys
from settings import *
from sprites import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
    
    def new(self):
        self.board = Board()
        self.board.displayBoard()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.draw()
        
        else:
            self.endScreen()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx //= tileSize
                my //= tileSize

                if event.button == 1:
                    if not self.board.boardList[mx][my].flagged:
                        # dig and explode
                        if not self.board.dig(mx, my):
                            # explode
                            for row in self.board.boardList:
                                for tile in row:
                                    if tile.flagged and tile.type != "X":
                                        tile.flagged = False
                                        tile.revealed = True
                                        tile.image = tileNotMine
                                    elif tile.type == "X":
                                        tile.revealed = True
                            self.playing = False

                if event.button == 3:
                    if not self.board.boardList[mx][my].revealed:
                        self.board.boardList[mx][my].flagged = not self.board.boardList[mx][my].flagged

                if self.checkWin():
                    self.win = True
                    self.playing = False
                    for row in self.board.boardList:
                        for tile in row:
                            if not tile.revealed:
                                tile.flagged = True
    
    def endScreen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return

    def checkWin(self):
        for row in self.board.boardList:
            for tile in row:
                if tile.type != "X" and not tile.revealed:
                    return False
        
        return True



    def draw(self):
        self.screen.fill(DARK_GREY) # Background color
        self.board.draw(self.screen)
        pygame.display.flip()

game = Game()
while True:
    game.new()
    game.run()
