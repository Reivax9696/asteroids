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
    
    def split(self):
        angle = random.uniform(20,50)
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        vel1 = self.velocity.rotate(angle) * 1.2 
        vel2 = self.velocity.rotate(-angle) * 1.2 
        
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vel1
        
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = vel2
    
        

    


    

