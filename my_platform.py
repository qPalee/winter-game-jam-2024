import pygame
import random

# fuck you python for making me use a different name for this file

class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = random.randint(70, 250)
        self.height = 10

    def draw(self, screen):
        pygame.draw.rect(screen, "#ff0000", pygame.Rect(self.x, self.y, self.width, self.height))

    def move(self, player_velocity):
        self.x += player_velocity

    def collides(self, player):
        platform_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        player_rect = pygame.Rect(player.x, player.y + player.height - 20, player.width, 20)

        return (platform_rect.colliderect(player_rect))
