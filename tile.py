import pygame
from abc import ABC

#position needs to be y, x
class Tile(ABC):
	def __init__(self, display = None, position = None):
		self.display = display
		self.position = position
	def display(self):
	#make it so it displays the right thing and goes to position
	    pass

class Bomb(Tile):
	def __init__(self, display = None, position = None):
		super().__init__(self, display, position)
		y, x = position
	
	def __str__(self):
		return "x"

	def display(self):
		screen.blit(thingies)

class Blank(Tile):
	def __init__(self, display = None, y = 0, x = 0):
		position = y, x
		super().__init(self, display, position)
		y, x = position
	
	def __str__(self):
		return "Blank"

	def display(self):
		screen.blit(thingies)

class Cover(Tile):
	def __init__(self, display = None, position = None):
		super().__init(self, display, position)
		y, x = position
		screen.blit(thingies)

	def __str__(self):
		return "Cover"
	
def clicked(self):
		del  self

class Number(Tile):
	def __init__(self, display = None, position = None, number = 0):
		super().__init(self, display, position)
		y, x = position

	def __str__(self):
		return self.display

	def display(self):
		screen.blit(thingies)