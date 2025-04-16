import pygame
import random
import sys
from constants import *
from os.path import join
from sprites import Player, Star, Meteor

def collisions():
    collision_sprites = pygame.sprite.spritecollide(player, meteor_sprites, False)
    if collision_sprites:
        sys.exit("Game over man!")
    
    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()

#General game setup
#Set the game window icon
icon = pygame.image.load("images/icon.png")
pygame.init()
pygame.display.set_icon(icon)
pygame.display.set_caption("Super Space Shooter")
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock()

#Imports
meteor_surface = pygame.image.load(join("images", "meteor.png")).convert_alpha()

#Sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
star_surface = pygame.image.load(join("images", "star.png")).convert_alpha()
for i in range(20):
    Star(all_sprites, star_surface)
player = Player(all_sprites)


#Meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

while running:
    #Game Loop
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x, y = random.randint(0, WINDOW_WIDTH), random.randint(-200, -100)
            Meteor(meteor_surface, (x, y), (all_sprites, meteor_sprites))

    #Updates
    all_sprites.update(dt, (all_sprites, laser_sprites))
    
    collisions()

    #Draw Game
    display_surface.fill("black")
    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit()