import pygame
import random
from constants import *

icon = pygame.image.load("images/icon.png")

pygame.init()
pygame.display.set_icon(icon)
pygame.display.set_caption("Super Space Shooter")
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

#Plain Surface
surf = pygame.Surface((100, 200))
surf.fill("black")
x = 100
y = 150

#Image Surface
player_surface = pygame.image.load("images/player.png").convert_alpha()
star_surface = pygame.image.load("images/star.png").convert_alpha()
star_positions = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
    #Game Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Draw Game
    #Background
    display_surface.fill("darkgrey")
    #Stars
    for pos in star_positions:
        display_surface.blit(star_surface, pos)
    #Player
    display_surface.blit(player_surface, (x, y))
    
    pygame.display.update()

pygame.quit()