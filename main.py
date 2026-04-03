# Game: tic-tac-tok 

import numpy as np
import pygame
import sys
from init import *
from objects import *
from functions import show, circle, cross, check_state
from constants import Game_board

turn = False 

show()
while True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for sq in range(len(sq_list)):
                if sq_list[sq].collidepoint(pos):
                    row, col = sq//3, sq%3
                    if Game_board[row][col] == 0:
                        if turn:
                            circle(sq)
                            turn = not turn
                            Game_board[row][col] = int(turn)+1 # player 1
                        else:
                            cross(sq)
                            turn = not turn
                            Game_board[row][col] = int(turn)+1 # player 2
                   # print(Game_board)

            state = check_state(Game_board)
            if state != "Continue":
                print(f"Player {state} wins!")
                pygame.quit()
                sys.exit()
    
    pygame.display.update()       

