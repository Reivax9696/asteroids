import pygame
from circleshape import CircleShape
import constants
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (128, 128, 128)

    def draw (self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    
        

    


    

