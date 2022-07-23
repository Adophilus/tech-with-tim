import pygame
import os
from utils.player import Player
from utils.enemy import Enemy

pygame.init()

BG = pygame.image.load(os.path.join("assets", "jumping_game", "Game", "bg.jpg"))
CHAR = pygame.image.load(os.path.join("assets", "jumping_game", "Game", "standing.png"))

FPS = 27
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 480
VEL = 10
RUN = True
X = 10
Y = SCREEN_HEIGHT - (10 + Player.HEIGHT)

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
OBJECTS = [ Player(WIN, X, Y) ]
OBJECTS.append(Enemy(OBJECTS[0], WIN, X+ 200, Y))

pygame.display.set_caption("First Game")

def redrawGameWindow ():
  global WALK_COUNT

  WIN.blit(BG, (0, 0))

  for o in OBJECTS:
    o.draw()

  pygame.display.update()

while (RUN):
  CLOCK.tick(FPS)

  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      RUN = False
    for o in OBJECTS:
      o.event(event)

  keys = pygame.key.get_pressed()
  for o in OBJECTS:
    o.keyPress(keys)

  redrawGameWindow()

pygame.quit()
