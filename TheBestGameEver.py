#this is where most or all of the code for the game will be contained
#We'll start by commenting the game and then fill in the rest with code later.
#open a game window
#show main menu screen
        #option to play
        #option for how to play
        #option high scores
        #game options
            #sound
            #game speed
            #start-length

        #create game objects
            #movable area
            #score
            #snake
            #apples - of different types
        #set stage for game
            #place snake
            #place the apple
    #main game loop begins
        #move snake
        #check for user input and adjust direction accordingly
        #when you eat an apple
            #increment score
            #add length to snake body
            #place new apple
        #check for collision with wall or self
            #if a collision occurs
                #end main game loop
    #show game over screen
    #ask user for name to save high score
    #display top scores
    #ask user to play again

print("Hello World!")
import sys, pygame

def main():
	pygame.init()

	size = width, height = 500, 500
	window = pygame.display.set_mode(size)
	pygame.display.set_caption('Best Snake Game')

	done = False
	color = (225, 255, 255)
	x = 30
	y = 30

	clock = pygame.time.Clock()

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP]: y -= 3
		if pressed[pygame.K_DOWN]: y += 3
		if pressed[pygame.K_LEFT]: x -= 3
		if pressed[pygame.K_RIGHT]: x += 3

		window.fill((0, 0, 0))
		pygame.draw.rect(window, color, pygame.Rect(x, y, 60, 60))

		pygame.display.flip()
		clock.tick(60)

if __name__ == '__main__':
	main()