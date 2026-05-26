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

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def draw(self):
        self.screen.fill(DARK_GREY) # Background color
        pygame.display.flip()

game = Game()
while True:
    game.new()
    game.run()
