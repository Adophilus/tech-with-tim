import pygame
import os

pygame.init()

BG = pygame.image.load(os.path.join("assets", "jumping_game", "Game", "bg.jpg"))
CHAR = pygame.image.load(os.path.join("assets", "jumping_game", "Game", "standing.png"))
WALK_LEFT = [ pygame.image.load(os.path.join("assets", "jumping_game", "Game", f"L{i}.png")) for i in range(1, 10) ]
WALK_RIGHT = [ pygame.image.load(os.path.join("assets", "jumping_game", "Game", f"R{i}.png")) for i in range(1, 10) ]

FPS = 27
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 480
VEL = 10
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64
RUN = True
LEFT = False
RIGHT = False
WALK_COUNT = 0
X = 10
Y = SCREEN_HEIGHT - (10 + PLAYER_HEIGHT)
PLAYER_COLOR = (0xef, 0xef, 0xef)
IS_JUMP = False
JUMP_COUNT = 10

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()

pygame.display.set_caption("First Game")

def redrawGameWindow ():
  global WALK_COUNT

  WIN.blit(BG, (0, 0))

  if (WALK_COUNT >= 27):
    WALK_COUNT = 0

  if (LEFT):
    WIN.blit(WALK_LEFT[WALK_COUNT // 3], (X, Y))
    WALK_COUNT += 1
  elif (RIGHT):
    WIN.blit(WALK_RIGHT[WALK_COUNT // 3], (X, Y))
    WALK_COUNT += 1
  else:
    WIN.blit(CHAR, (X, Y))
  pygame.display.update()

while (RUN):
  CLOCK.tick(FPS)

  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      RUN = False

  keys = pygame.key.get_pressed()

  if (keys[pygame.K_LEFT] and (X - VEL) > 0):
    X -= VEL
    LEFT = True
    RIGHT = False
  elif (keys[pygame.K_RIGHT] and (X + VEL + PLAYER_WIDTH) < SCREEN_WIDTH):
    X += VEL
    LEFT = False
    RIGHT = True
  else:
    LEFT = False
    RIGHT = False
    WALK_COUNT = 0

  if (not IS_JUMP):
    if (keys[pygame.K_SPACE]):
      IS_JUMP = True
      LEFT = False
      RIGHT = False
  else:
    if (JUMP_COUNT >= -10):
      NEG = 1
      if (JUMP_COUNT < 0):
        NEG = -1
      Y -= JUMP_COUNT ** 2 * 0.5 * NEG
      JUMP_COUNT -= 1
    else:
      IS_JUMP = False
      JUMP_COUNT = 10  

  redrawGameWindow()

pygame.quit()