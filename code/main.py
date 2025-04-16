import pygame
import random
from constants import *
from os.path import join
from sprites import Player, Star

#General game setup
#Set the game window icon
icon = pygame.image.load("images/icon.png")
pygame.init()
pygame.display.set_icon(icon)
pygame.display.set_caption("Super Space Shooter")
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock()

#Plain Surface
surf = pygame.Surface((100, 200))
surf.fill("black")

all_sprites = pygame.sprite.Group()
star_surface = pygame.image.load(join("images", "star.png")).convert_alpha()
for i in range(20):
    Star(all_sprites, star_surface)
player = Player(all_sprites)

#Join method here is another way to tell this load method where the file is located.
meteor_surface = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rectangle = meteor_surface.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 100))

laser_surface = pygame.image.load("images/laser.png").convert_alpha()
laser_rectangle = meteor_surface.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))

while running:
    #Game Loop
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Updates
    all_sprites.update(dt)

    #Draw Game
    display_surface.fill("black")
    all_sprites.draw(display_surface)
    pygame.display.update()

pygame.quit()