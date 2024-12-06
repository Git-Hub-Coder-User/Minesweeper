import pygame
from abc import ABC, abstractmethod

#position needs to be y, x
class Tile(ABC):
	def __init__(self, display = None, position = None):
		self.display = display
		self.position = position
	
	def display(self, position):
		y, x = position
		if (y + x) % 2 == 0:
			y = (y * 100) + 50
			x = (x * 100) + 50

			self.tile = pygame.image.load("img/dark_tile.png").convert_alpha()
			self.tile = pygame.transform.scale(self.tile, (50, 50))
			self.tile_rect = self.tile.get_rect(center = (y, x))
		
		if (y + x) % 2 == 1:
			y = (y * 100) + 50
			x = (x * 100) + 50

			self.tile = pygame.image.load("img/light_tile.png").convert_alpha()
			self.tile = pygame.transform.scale(self.tile, (50, 50))
			self.tile_rect = self.tile.get_rect(center = (y, x))

class Bomb(Tile):
	def __init__(self, display = None, position = None):
		super().__init__(display, position)
		y, x = position
	
	def __str__(self):
		return "x"

	def display(self, position):
		# screen.blit(thingies)
		pass


		

class Blank(Tile):
	def __init__(self, display = None, position = None):
		super().__init__(display, position)
		y, x = position
	
	def __str__(self):
		return "Blank"


class Cover(Tile):
	def __init__(self, display = None, position = None):
		super().__init__(display, position)
		y, x = position
		# screen.blit(thingies)


	def __str__(self):
		return "Cover"
	
def clicked(self):
		del self

class Number(Tile):
	def __init__(self, display = None, position = None, number = 0):
		super().__init__(display, position)
		y, x = position

	def __str__(self):
		return self.display

	def display(self):
		# screen.blit(thingies)
		pass