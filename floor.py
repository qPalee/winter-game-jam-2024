import pygame
from player import Player

class Floor:
    def __init__(self, y):
        self.x = 0
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, '#ff0000', 
                        pygame.Rect(self.x, self.y, 
                        screen.get_width(),
                        (screen.get_height() * (1 - 1/16))))
        
    def collides(self, player, screen):
        floorRect = pygame.Rect(self.x, self.y, 
                        screen.get_width(),
                        (screen.get_height() * (1 - 1/16)))
        
        playerRect = pygame.Rect(player.x, player.y, player.width, player.height)

        return (floorRect.colliderect(playerRect))
        
        
