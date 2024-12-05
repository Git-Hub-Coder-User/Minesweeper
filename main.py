import pygame
import sys
from grid import Grid
from tile import(
    Tile, 
    Blank, 
    Number, 
    Cover, 
    Bomb
)


def main():
    background = Grid()
    background.generate_bombs()
    background.convert_grid()
    background.visual_set_up()

    foreground = Grid(Cover)
    # foreground.convert_grid()
    foreground.visual_set_up()

    # back = 

    pygame.init()
    screen = pygame.display.set_mode((400, 400))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("This exists")
                pygame.quit()
                sys.exit()
    
    
        screen.blit(back, (0,0))

main()