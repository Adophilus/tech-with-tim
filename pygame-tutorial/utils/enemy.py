import os
import pygame
from utils.player import Player

class Enemy (Player):
  WALK_LEFT = [ pygame.image.load(os.path.join("assets", "jumping_game", "Game", f"L{i}E.png")) for i in range(1, 10) ]
  WALK_RIGHT = [ pygame.image.load(os.path.join("assets", "jumping_game", "Game", f"R{i}E.png")) for i in range(1, 10) ]

  def __init__ (self, player, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.player = player
    
  def keyPress (self, event):
    pass

  def draw (self):
    if (self.player.x < self.x):
      self.left = True
      self.right = False
    else:
      self.left = False
      self.right = True
    self._shootBullet()
    super().draw()