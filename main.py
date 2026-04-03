# Game: tic-tac-tok 

import pygame
import sys
from init import *
from objects import *
from functions import show, circle, cross


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
                    cross(sq)

    
    pygame.display.update()       

