import pygame

class Game:
    def __init__(self, background_img):
        self.background = pygame.image.load(background_img).convert_alpha()
    
    def resize_img(self):
        self.background = pygame.transform.scale(self.background, (400, 400))
