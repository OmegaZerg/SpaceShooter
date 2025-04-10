import pygame
from constants import *

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

while running:
    #Game Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Draw Game

pygame.quit()