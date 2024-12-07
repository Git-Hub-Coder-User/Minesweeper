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
    game = Game("img/backgroud_img.png")
    game.resize_img()
    # background = Grid()
    # background.generate_bombs()
    # print(background)
    # background.convert_grid()
    # background.visual_set_up()

    foreground = Grid(Cover)
    foreground.convert_grid()
    foreground.visual_set_up()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


main()
# print(background)