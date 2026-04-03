import pygame
import sys
from init import *
from constants import *



while True:
    game_display.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()       

