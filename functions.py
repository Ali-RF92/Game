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
    

def cross(i):
    row, col = i//3, i%3
    pygame.draw.line(game_display, 
                     blue, 
                     (CORDS[col]+20, CORDS[row]+20), (CORDS[col]+TILE_SIZE-20, CORDS[row]+TILE_SIZE-20),
                       7)
    
    pygame.draw.line(game_display, 
                     blue, 
                     (CORDS[col]+20, CORDS[row]+TILE_SIZE-20), (CORDS[col]+TILE_SIZE-20, CORDS[row]+20),
                       7)
    
    
    
    