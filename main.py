import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player1 = Player(x=constants.SCREEN_WIDTH / 2, y=constants.SCREEN_HEIGHT / 2)
    asteroid1 = Asteroid( x=100, y=100, radius=30)
    updatable.add(player1)
    drawable.add(player1)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)
    running = True  
    
    while running:
        dt = clock.tick(60) / 1000.0
        
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                running = False
        

        updatable.update(dt)

        for asteroid in asteroids:
            if player1.collision(asteroid):
                print("Game Over!")
                pygame.quit()

        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
            
                
        
        screen.fill((0, 0, 0))
        

        for sprite in drawable:
            sprite.draw(screen)
        
        
        pygame.display.flip()
        

    pygame.quit()

if __name__ == "__main__":
    main()