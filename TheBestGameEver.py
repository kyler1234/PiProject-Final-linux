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
from pygame import *	#needed to reference keys directly instead of pygame.K_xxxx

#directional constants
DIRECTION_UP = 0
DIRECTION_DOWN = 1
DIRECTION_LEFT = 2
DIRECTION_RIGHT = 3

#look up table for keys and directions, we can add joystic movement as well
KEY_DIRECTION = {
    K_w: DIRECTION_UP,    K_UP:    DIRECTION_UP,   
    K_s: DIRECTION_DOWN,  K_DOWN:  DIRECTION_DOWN, 
    K_a: DIRECTION_LEFT,  K_LEFT:  DIRECTION_LEFT, 
    K_d: DIRECTION_RIGHT, K_RIGHT: DIRECTION_RIGHT,
}

#color constants in RGB
SNAKE_HEAD_COLOR = (250, 50, 50)
SNAKE_BODY_COLOR = (250, 250, 250)
APPLE_COLOR = (50, 250, 50)
BACKGROUND_COLOR = (0, 0, 0)

#grid size constant
GRID = (50, 50) # X, Y

#snake based constants
SNAKE_SPEED_INITIAL = 4.0       # Initial snake speed
SNAKE_SPEED_INCREMENT = 0.25    # Snake speeds up this much each time it grows
SNAKE_START_LENGTH = 4          # Initial snake length in segments
SNAKE_START_LOC = (25, 25)    # Initial snake location

#snake class
#init with a starting point as a tupple and length in number of grid squares
class Snake:
    def __init__ (self, start, length):
        self.startLength = startLength
        self.speed = SNAKE_SPEED_INITIAL
        self.start = start
        self.reset()

    #reset snake to original state
    def reset(self):
        self.snakeBits = []
        self.direction = DIRECTION_UP

        for n in range(0, self.startLength):
            self.snakeBits.append((self.start[0], self.start[1] + n))

    #change directions if not in opposite direciton
    def change_direction(self, direction):
        if not (self.direction == 0 and direction == 1 or
            self.direction == 1 and direction == 0 or
            self.direction == 2 and direction == 3 or
            self.direction == 3 and direction == 2):
        	self.direction = direction

    # Returns the head of the snake
    def getHead(self):
        return self.snakeBits[0]

    # Returns the tail of the snake
    def getTail(self):
        return self.snakeBits[len(self.snakeBits) - 1]

    #return the entire snake
    def getSnake(self):
    	return self.snakeBits

    #move the snake by 1 block in a direction
    def move_snake(self):
        head = self.getHead();
        newHead = ()

        if self.direction == 0: newHead = (head[0], head[1] + 1)
        if self.direction == 1: newHead = (head[0], head[1] - 1)
        if self.direction == 2: newHead = (head[0] + 1, head[1])
        if self.direction == 3: newHead = (head[0] - 1, head[1])

        self.snakeBits.pop()
        self.snakeBits.insert(0, newHead)

    #add bits to the end of the snake
    def add_bit(self):
        tail = self.getTail();
        bit = ()

        if self.direction == 0: bit = (tail[0], tail[1] + 1)
        if self.direction == 1: bit = (tail[0], tail[1] - 1)
        if self.direction == 2: bit = (tail[0] + 1, tail[1])
        if self.direction == 3: bit = (tail[0] - 1, tail[1])

        self.snakeBits.append(bit)

    #check if the head is located in the same cell as another bit of the snake
    def check_collision(self):
        if len([bit for bit in self.snakeBits if bit == self.getHead()]) > 1:
            return True
        else:
            return False

class Food:
	def __init__(self, snake):
		self.location = (0,0)
		self.foods = []
		self.snake = snake

	def reset(self):
		self.foods = []
		self.spawn()

	#method to spawn food at random location
	def spawn(self):
		self.location = __randomLocation()
		#check if it spawns on snake, else relocate
		while self.location == (bit for bit in snake):
			self.location = (__randomLocation())
		self.food.append(self.location)
		return self.foods

	#check if any of the foods is eaten if so remove from foods
	def is_eaten(self):
		if (food for food in self.foods) == snake.getHead():
			self.foods.pop(index(food))
			return True
		else:
			return False

	#returns all foods alive
	def get_foods(self):
		return self.foods

	#private method for food spawns
	def __randomLocation(self):
		randX = random.randint(0,GRID[0])
		randY = random.randint(0,GRID[1])
		return (randX, randY)

class Game:
	def __init__(self, window, screen, clock, font):
		self.window = window
		self.screen = screen
		self.clock = clock
		self.font = font

		self.fps = STARTING_FPS
		self.ticks = 0
		self.playing = False
		self.main_menu = True
		self.score = 0
		self.world = Rect((0,0), GRID)

		self.nextDirection = DIRECTION_UP
		self.snake = Snake(SNAKE_START_LOC, SNAKE_START_LENGTH)
		self.food = Food(snake)

	def play(self):
		pass

	def draw():
		self.screen.fill(BACKGROUND_COLOR)
		

	def reset(self):
		self.snake.reset()
		self.food.reset()

	def input(self, events):
		#movement
		if events.key in KEY_DIRECTION:
			self.nextDirection = KEY_DIRECTION[e.key]
		elif e.key == K_ESCAPE and not self.playing:
			#go to main menu code here
			pass

	def update(self):
		self.snake.changeDirection(self.nextDirection)
		self.snake.update()

		if food.is_eaten():
			self.snake.add_bit()
			#score code
		if self.snake.check_collision() or  self.world.collidepoint(self.snake.getHead()):
			self.playing = False
			#game over screen



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