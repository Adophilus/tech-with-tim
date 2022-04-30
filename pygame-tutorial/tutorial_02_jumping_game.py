import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
VEL = 10
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30
RUN = True
X = 10
Y = SCREEN_HEIGHT - (10 + PLAYER_HEIGHT)
PLAYER_COLOR = (0xef, 0xef, 0xef)
IS_JUMP = False
JUMP_COUNT = 10

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("First Game")

while (RUN):
  pygame.time.delay(50)

  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      RUN = False

  keys = pygame.key.get_pressed()

  if (keys[pygame.K_LEFT] and (X - VEL) > 0):
    X -= VEL
  if (keys[pygame.K_RIGHT] and (X + VEL + PLAYER_WIDTH) < SCREEN_WIDTH):
    X += VEL

  if (not IS_JUMP):
    if (keys[pygame.K_UP] and (Y - VEL) > 0):
      Y -= VEL
    if (keys[pygame.K_DOWN] and (Y + VEL + PLAYER_HEIGHT) < SCREEN_HEIGHT):
      Y += VEL
    if (keys[pygame.K_SPACE]):
      IS_JUMP = True
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

  WIN.fill((0, 0, 0))
  pygame.draw.ellipse(WIN, PLAYER_COLOR, (X, Y, PLAYER_WIDTH, PLAYER_HEIGHT))
  pygame.display.update()

pygame.quit()