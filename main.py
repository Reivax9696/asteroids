import pygame
import constants
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player1 = Player(x=constants.SCREEN_WIDTH / 2, y=constants.SCREEN_HEIGHT / 2)
    updatable.add(player1)
    drawable.add(player1)
    running = True  
    
    while running:
        dt = clock.tick(60) / 1000.0
        
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                running = False
        
		#Update player situation
        updatable.update(dt)
        
        screen.fill((0, 0, 0))
        
		#Draw the sprites in drawable
        for sprite in drawable:
            sprite.draw(screen)
        
        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()