import os
import pygame
# Colors for the game (R, G, B)
WHITE = (255,255,255)
BLACK = (0,0,0)
DARK_GREY = (40,40,40)
LIGHT_GREY = (100,100,100)
GREEN = (0,255,0)
DARK_GREEN = ()
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)



# Actual settings for the game
tileSize = 32
rows = 15
cols = 15
amountOfMines = 5
width = tileSize * cols
height = tileSize * rows
title = "Minesweeper"
fps = 60

tileNumbers = []
for i in range(1,9):
    tileNumbers.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", f"Tile{i}.png")), (tileSize,tileSize)))

tileEmpty = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileEmpty.png")), (tileSize,tileSize))
tileExploded = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileExploded.png")), (tileSize,tileSize))
tileFlag = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileFlag.png")), (tileSize,tileSize))
tileMine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileMine.png")), (tileSize,tileSize))
tileNotMine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileNotMine.png")), (tileSize,tileSize))
tileUnknown = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileUnknown.png")), (tileSize,tileSize))
