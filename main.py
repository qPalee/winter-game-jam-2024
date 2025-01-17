import pygame
import random

from player import Player
from my_platform import Platform
from floor import Floor

def spawnPlatforms(platforms):
    if(len(platforms) >= 3):
        return
    
    # theres defo a better way of doing this but im too tired to think of it rn
    # if you are reading this I did NOT change it :)
    
    rng_number = random.random()
    if(rng_number < 0.5): # 50% chance to spawn 1 platform
        platforms.append(Platform(random.randint(520, 800), random.randint(256, 384)))
        return
    
    if(rng_number < 0.8): # 0.5 < rng_number < 0.8 -> 30% chance to spawn 2 platforms
        platforms.append(Platform(random.randint(520, 800), random.randint(256, 384)))
        platforms.append(Platform(random.randint(820, 1024), random.randint(384, 512)))
        return
    
    # rng_number > 0.8 -> 20% chance to spawn 3 platforms
    platforms.append(Platform(random.randint(520, 800), random.randint(256, 384)))
    platforms.append(Platform(random.randint(820, 1024), random.randint(384, 512)))
    platforms.append(Platform(random.randint(1200, 1300), random.randint(384, 512)))

def modifyPlatforms(platforms):
    for i in range(len(platforms)):
        if(platforms[i].x < -platforms[i].width):
            platforms.pop(i)
            if(len(platforms) < 3):
                spawnPlatforms(platforms)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player = Player()
platforms = []
platforms.append(Platform(random.randint(520, 800), random.randint(256, 384)))
spawnPlatforms(platforms)

floor = Floor((screen.get_height() * (1 - 1/16)))

movement_speed = 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement

    keys = pygame.key.get_pressed()
    mods = pygame.key.get_mods()

    player.calculateSpeed(keys)
    player.move(screen)

    for p in platforms:
        p.move(-player.x_velocity)
        if(p.collides(player) and player.y_velocity > 0):
            player.y = p.y - player.height + 1
            player.y_velocity = 0
            player.on_ground = True
        else:
            player.on_ground = False

    if(floor.collides(player, screen)):
        player.y = floor.y - player.height + 1
        player.y_velocity = 0
        player.on_ground = True

    # Drawing shit to the buffer
            
    screen.fill("black")

    player.draw(screen)
    for p in platforms:
        p.draw(screen)

    floor.draw(screen)

    # Display buffer
    pygame.display.flip()

    clock.tick(60)

pygame.quit()