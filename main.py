# Game: tic-tac-tok 

import pygame
import sys
from init import *
from constants import *
from objects import *


def show():
    for sq in sq_list:
        pygame.draw.rect(game_display, white, sq)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    show()
    pygame.display.update()       

