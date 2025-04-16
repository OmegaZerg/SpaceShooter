import pygame
import random
from constants import *
from os.path import join

#Set the game window icon
icon = pygame.image.load("images/icon.png")

pygame.init()
pygame.display.set_icon(icon)
pygame.display.set_caption("Super Space Shooter")
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
player_direction = 1

#Plain Surface
surf = pygame.Surface((100, 200))
surf.fill("black")
x = 100
y = 150

#Image Surfaces
player_surface = pygame.image.load("images/player.png").convert_alpha()
player_rectangle = player_surface.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

#Join method here is another way to tell this load method where the file is located.
meteor_surface = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rectangle = meteor_surface.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 100))

laser_surface = pygame.image.load("images/laser.png").convert_alpha()
laser_rectangle = meteor_surface.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))

star_surface = pygame.image.load("images/star.png").convert_alpha()
star_positions = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
    #Game Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Draw Game
    #Background
    display_surface.fill("black")
    
    #Stars
    for pos in star_positions:
        display_surface.blit(star_surface, pos)
    
    #Meteor
    display_surface.blit(meteor_surface, meteor_rectangle)

    #Laser
    display_surface.blit(laser_surface, laser_rectangle)
    
    #Player
    #Moves player to right until edge of screen
    # if player_rectangle.right < WINDOW_WIDTH:
    #     player_rectangle.left += 0.1
    
    #Moves player to left until edge of screen
    # if player_rectangle.left > 0:
    #     player_rectangle.left -= 0.1

    #Bounce player left to right
    player_rectangle.left += player_direction * 0.2
    if player_rectangle.right > WINDOW_WIDTH or player_rectangle.left < 0:
        player_direction *= -1

    display_surface.blit(player_surface, player_rectangle)

    pygame.display.update()

pygame.quit()