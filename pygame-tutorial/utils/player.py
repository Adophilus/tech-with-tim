import pygame
import os
from utils.player_bullet import PlayerBullet

class Player ():
  WALK_LEFT = [ pygame.image.load(os.path.join("assets", "jumping_game", "Game", f"L{i}.png")) for i in range(1, 10) ]
  WALK_RIGHT = [ pygame.image.load(os.path.join("assets", "jumping_game", "Game", f"R{i}.png")) for i in range(1, 10) ]
  PLAYER = pygame.image.load(os.path.join("assets", "jumping_game", "Game", f"standing.png"))
  WALK_COUNT = 0
  WIDTH = 64
  HEIGHT = 64
  KEY_LEFT = pygame.K_a
  KEY_RIGHT = pygame.K_d
  KEY_JUMP = pygame.K_w
  KEY_SHOOT = pygame.K_j
  BULLETS = [ ]
  BULLETS_LIMIT = 5

  def __init__ (self, window, x: int, y: int, width: int = 64, height: int = 64, vel: int = 10):
    self.window = window
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.vel = vel
    self.left = False
    self.right = False
    self.isJump = False
    self.jumpCount = 10
    self.standing = True
    self.screenWidth, self.screenHeight = self.window.get_size()

  def draw (self):
    if (self.WALK_COUNT >= 27):
      self.WALK_COUNT = 0

    if (not self.standing):
      if (self.left):
        self.window.blit(self.WALK_LEFT[self.WALK_COUNT // 3], (self.x, self.y))
        self.WALK_COUNT += 1
      elif (self.right):
        self.window.blit(self.WALK_RIGHT[self.WALK_COUNT // 3], (self.x, self.y))
        self.WALK_COUNT += 1
    else:
      if (self.right):
        self.window.blit(self.WALK_RIGHT[0], (self.x, self.y))
      else:
        self.window.blit(self.WALK_LEFT[0], (self.x, self.y))

    for bullet in self.BULLETS:
      if (not bullet.shouldDraw):
        self.BULLETS.remove(bullet)
        continue
      bullet.draw()

  def event (self, event):
    pass

  def keyPress (self, keys: list):
    if (keys[self.KEY_LEFT] and (self.x - self.vel) > 0):
      self.move("left")
    elif (keys[self.KEY_RIGHT] and (self.x + self.vel + self.width) < self.screenWidth):
      self.move("right")
    else:
      self.standing = True
      WALK_COUNT = 0

    if (keys[self.KEY_SHOOT]):
      self._shootBullet()

    if (not self.isJump):
      if (keys[self.KEY_JUMP]):
        self.isJump = True
    else:
      if (self.jumpCount >= -10):
        NEG = 1
        if (self.jumpCount < 0):
          NEG = -1
        self.y -= self.jumpCount ** 2 * 0.5 * NEG
        self.jumpCount -= 1
      else:
        self.isJump = False
        self.jumpCount = 10 

  def move (self, direction: str):
    direction = direction.lower()
    if (direction == "left"):
      return self._moveLeft()
    elif (direction == "right"):
      return self._moveRight()

  def _moveLeft (self):
    self.x -= self.vel
    self.left = True
    self.right = False
    self.standing = False

  def _moveRight (self):
    self.x += self.vel
    self.left = False
    self.right = True
    self.standing = False

  def _shootBullet (self):
    if (len(self.BULLETS) < self.BULLETS_LIMIT):
      facing = 1 if self.right else -1
      self.BULLETS.append(PlayerBullet(self.window, self.x + (self.WIDTH // 2), self.y + (self.HEIGHT // 2), facing = facing))
