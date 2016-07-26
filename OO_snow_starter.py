"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random
from PIL import Image


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
greyish = (193, 205, 205)
LIGHT_BLUE = (187, 255, 255)
OTHER_LIGHT_BLUE = (202, 225, 255)
OTHER_GREY = (122, 139, 139)
OTHER_BLUE = (100, 139, 137)
ANOTHER_ONE = (173, 216, 230)
ORANGE = (255, 157, 0)
BROWN = (139, 69, 0)

SNOW_COLOR_LIST = [greyish, LIGHT_BLUE, OTHER_LIGHT_BLUE, OTHER_GREY, OTHER_BLUE, WHITE]
snowflake_list = []


image = pygame.image.load("snowy9.jpg")
#image.show()
pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


class SnowFlake():
	'''
    This class will be used to create the SnowFlake Objects.
    It takes: 
        size - an integer that tells us how big we want the snowflake
        position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
        wind - a boolean that lets us know if there is any wind or not.  
	'''

	def __init__(self, size, position, wind=False): #if no wind var is given, false is default
		self.size = size
		self.position = position
		self.wind = wind
    
    
	def fall(self, speed):
		"""
        Take in a integer that represnts the speed at which the snowflake is falling in the y-direction.  
        A positive integer will have the snowflake falling down the screen. 
        A negative integer will have the snowflake falling up the screen. 
        
        If wind = True
            - the x direction of the snowflake changes
		"""
		self.position[1] += speed
		if self.wind == True:
			self.position[0] += speed/2
		
        
	def draw(self):
		"""
        Uses pygame and the global screen variable to draw the snowflake on the screen
		"""
		global screen
		global SNOW_COLOR_LIST
		SNOW_COLOR = SNOW_COLOR_LIST[random.randint(0, len(SNOW_COLOR_LIST) - 1)]
		pygame.draw.circle(screen, SNOW_COLOR, self.position, self.size)
        

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed
speed = 1

#Drawing a snowman

#INITIALIZE YOUR SNOWFLAKE HERE! 
for x in range (2):	
	snowflake_list.append(SnowFlake(random.randint(0, 4), [random.randint(10, 700), 10]))

# Snow List

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
	#screen.fill(BLACK)
	screen.blit(image, [0, 0])

    # --- Drawing code should go here
    # Begin Snow
	pygame.draw.circle(screen, WHITE, [115, 425], 60)
	pygame.draw.circle(screen, WHITE, [115, 330], 45)
	pygame.draw.circle(screen, WHITE, [115, 260], 35)
	pygame.draw.circle(screen, BLACK, [103, 250], 5)
	pygame.draw.circle(screen, BLACK, [125, 250], 5)
	pygame.draw.rect(screen, BLACK, (80, 220, 75, 10), 0)
	pygame.draw.rect(screen, BLACK, (95, 175, 40, 50), 0)
	pygame.draw.arc(screen, RED, [95, 255, 40, 20], 3.14, 6.28, 2)
	pygame.draw.polygon(screen, ORANGE, [(110,255), (125, 265), (110, 265)], 0)
	pygame.draw.circle(screen, BLUE, [115, 305], 6)
	pygame.draw.circle(screen, BLUE, [115, 325], 6)
	pygame.draw.circle(screen, BLUE, [115, 345], 6)
	pygame.draw.rect(screen, BROWN, (155, 330, 50, 5), 0)
	pygame.draw.rect(screen, BROWN, (32, 330, 50, 5), 0)
	pygame.draw.rect(screen, GREEN, (92, 285, 45, 10), 0)
	pygame.draw.rect(screen, GREEN, (90, 285, 9, 50), 0)
	#pygame.draw.rect(screen, GREEN, (100, 285, 9, 65), 0)
	pygame.draw.rect(screen, RED, (95, 212, 40, 7), 0)
	pygame.draw.circle(screen, RED, [205, 332], 10)
	pygame.draw.circle(screen, RED, [32, 332], 10)

	
	z = 0
	for y in snowflake_list:
		snowflake_list[z].draw()
		snowflake_list[z].fall(random.randint(1, 5))
		z += 1
    


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	for x in range (2):	
		snowflake_list.append(SnowFlake(random.randint(0, 4), [random.randint(10, 700), 10]))

    # --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
