import pygame
from init import *
from objects import *
from constants import *


def show():
    for sq in sq_list:
        pygame.draw.rect(game_display, white, sq)


def circle(i):
    row, col = i//3, i%3    
    pygame.draw.circle(game_display,
                        red,
                        (CORDS[col]+HALF_TILE, CORDS[row]+HALF_TILE),
                        50, 7)