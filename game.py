import pygame

class Game:
    def __init__(self, screen, background_img):
        self.background = pygame.image.load(background_img).convert_alpha()
        # self.background = pygame.transform.scale(self.background, (400, 400))
    
    def show_background(self, screen):
        screen.blit(self.background, (0,0))