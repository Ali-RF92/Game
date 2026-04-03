import pygame
from init import *
from objects import *
from constants import *
import numpy as np
import sys


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
    
    
    
def check_state(game_board):
    for i in range(3):
        row = np.unique(game_board[:,i])
        col = np.unique(game_board[i,:])

        if len(row) == 1 and row!=0:
            return row
        
        if len(col) == 1 and col!=0:
            return col
        
        
    if game_board[0][0] == game_board[1][1] and game_board[1][1] == game_board[2][2] and game_board[0][0] !=0: 
        return game_board[0][0]
    
    elif game_board[2][0] == game_board[1][1] and game_board[1][1] == game_board[0][2] and game_board[2][0] !=0:
        return game_board[1][1]
    
    
    
    if 0 not in np.unique(game_board):
        return "Tie"
    

    return "Continue"


def restart():
    return np.array([[0,0,0], [0,0,0], [0,0,0]])