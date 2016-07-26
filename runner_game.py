# Runner Game
# 07/15/2016

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Runner Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# import city scroller file
from city_scroller_rg import Scroller

FRONT_SCROLLER_COLOR = (0, 237, 203) # TURQ
BACKGROUND_COLOR = (189, 246, 255) # LIGHT BLUE

front_scroller = Scroller(SCREEN_WIDTH, 300, SCREEN_HEIGHT-10, FRONT_SCROLLER_COLOR, 3)

front_scroller.add_buildings()
a = 0

all_sprites_list = []

class RunnerSprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("pikachu.jpg")	
		self.image = pygame.transform.scale(self.image, (95, 65)) # re-sizes image
		self.image = pygame.transform.flip(self.image, True, False) # rotates image
		self.rect = self.image.get_rect()
	def draw(self, mouse_pos):
		screen.blit(self.image, mouse_pos)
		all_sprites_list.append(self.image)		

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Game logic should go here
	if a % 40 == 0:
		front_scroller.add_building(-100)
	a += 1
	
	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.
	screen.fill(BACKGROUND_COLOR)
	
	mouse_pos = pygame.mouse.get_pos()  #get mouse position
	
	# --- Drawing code should go here

	front_scroller.draw_buildings()
	front_scroller.move_buildings()
	
	runner = RunnerSprite()
	runner.rect.move(mouse_pos)
	runner.rect.x = mouse_pos[0]
	runner.rect.y = mouse_pos[1]

	runner.draw(mouse_pos)
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(30)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
