import pygame
import sys
from grid import Grid
from game import Game
from tile import(
    Tile, 
    Blank, 
    Number, 
    Cover, 
    Bomb
)

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                y, x = pygame.mouse.get_pos()
                y = (y - 25) / 50
                x = (x - 25) / 50
                foreground.delete(y, x)

        game = Game(screen, "img/backgroud_img.png")
        # game.show_background(screen)

        background = Grid()
        background.generate_bombs()
        background.convert_grid()
        background.visual_set_up(screen)

        foreground = Grid(Cover)
        foreground.visual_set_up(screen)



main()
# print(background)