import pygame
from pygame import rect

class Player:
    def __init__(self):
        self.x = 480
        self.y = 640
        self.width = 50
        self.height = 100
        self.on_ground = True
        self.x_velocity = 2
        self.y_velocity = 0
        self.gravity = 9.8

    def draw(self, screen):
        pygame.draw.rect(screen, "#00ffff", pygame.Rect(self.x, self.y, self.width, self.height))

        player_rect = pygame.Rect(self.x, self.y + self.height - 10, self.width, 15)
        pygame.draw.rect(screen, "#ffffff", player_rect)

    def calculateSpeed(self, keys):
        if(self.on_ground):
            if(keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]): 
                self.y_velocity -= 144
                self.on_ground = False
            
    def move(self, screen):
        self.y_velocity += self.gravity
        self.y_velocity *= 0.9

        if(not self.on_ground):
            self.y += self.y_velocity
            if(self.y < 0):
                self.y = 0
                self.y_velocity = 0

        if(self.y + self.height > screen.get_height()):
            self.y = screen.get_height() - self.height

    



