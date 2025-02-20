import pygame
import constants



def main ():
	pygame.init()
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	number = True
	while number == True:
		for event in pygame.event.get():
   			 if event.type == pygame.QUIT:
        		 	return	
		screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
		screen.fill((0, 0, 0))
		pygame.display.flip()

	
	



if __name__ == "__main__":
    main()
