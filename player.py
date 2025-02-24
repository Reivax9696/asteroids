import pygame
from circleshape import CircleShape
import constants
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        triangle_points = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), [(int(p.x), int(p.y)) for p in triangle_points], 2)
        
    def rotate (self, dt, direction):
        self.rotation += constants.PLAYER_TURN_SPEED * dt * direction
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt, direction=-1)
        if keys[pygame.K_d]:
            self.rotate(dt, direction=1)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
        
        self.timer -= dt
    
    def move (self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
        shoot_velocity = pygame.Vector2(0,1).rotate(self.rotation) * constants.PLAYER_SHOT_SPEED
        shot.velocity = shoot_velocity
        self.timer = constants.PLAYER_SHOOT_COOLDOWN

        
            
            
            
