import pygame
import os

class PlayerBullet ():
	COLOR = (0, 0, 0)
	WIDTH = 15
	HEIGHT = 10
	VEL = 12
	shouldDraw = True

	def __init__ (self, window, x: int, y: int, color: tuple = None, facing = 1):
		self.x = x
		self.y = y
		self.window = window
		self.color = self.COLOR
		if (color):
			self.color = color
		self.facing = facing
		self.vel = self.VEL * facing
		self.screenWidth, self.screenHeight = self.window.get_size()

	def draw (self):
		if (self.shouldDraw):
			if (self.x > 0 and (self.x + self.WIDTH) < self.screenWidth):
				pygame.draw.rect(self.window, self.color, (self.x, self.y, self.WIDTH, self.HEIGHT))
				self.x += self.VEL * self.facing
			else:
				self.shouldDraw = False