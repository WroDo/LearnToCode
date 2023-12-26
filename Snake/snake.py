# Nah: https://docs.python.org/3/howto/curses.html
# Yeah: https://www.pygame.org/docs/
## apt-get install python3-pygame

import pygame
import random

# globals
gScreenSizeX=640;
gScreenSizeY=480;
pygame.init()
gRunning = True
gColorBackground="black"
gRectangleSize=20
gSnakePositions=list()
gSnakePositions.append(pygame.Vector2(int(gScreenSizeX/2)-1, int(gScreenSizeY/2)-1))
gDirection="right"
gTilesX=int(gScreenSizeX / gRectangleSize)
gTilesY=int(gScreenSizeY / gRectangleSize)
gPowerpillPosition=pygame.Vector2(random.randrange(1,gTilesX-1)*gRectangleSize-1, random.randrange(1,gTilesY-1)*gRectangleSize-1)
print("gPowerpillPosition: " + str(gPowerpillPosition))
gPowerpillCounter=0
gFontSize=36
gScore=0
gColorText="white"

# pygame setup
gScreen = pygame.display.set_mode((gScreenSizeX, gScreenSizeY))
gClock = pygame.time.Clock()
gFont = pygame.font.Font(pygame.font.get_default_font(), gFontSize)

# Functions
def printScore():
	lTextSurface = gFont.render("Score: " + str(gScore), True, gColorText)
	gScreen.blit(lTextSurface, dest=(gScreenSizeX/2-(lTextSurface.get_width() /2), gFontSize))

def wait():
	global gSnakePositions, gScore
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("QUIT")
				pygame.quit()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: # https://www.pygame.org/docs/ref/key.html
				print("KEYDOWN")
				gSnakePositions=list()
				gSnakePositions.append(pygame.Vector2(int(gScreenSizeX/2)-1, int(gScreenSizeY/2)-1))
				gScore=0
				return

# Main
while gRunning:
	# poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
			gRunning = False

	# Read keyboard event and set coordinates of head (new rect)
	lKeys = pygame.key.get_pressed()
	if lKeys[pygame.K_w] or lKeys[pygame.K_UP]: #up
		print("up")
		gDirection="up"
	if lKeys[pygame.K_s] or lKeys[pygame.K_DOWN]: #down
		print("down")
		gDirection="down"
	if lKeys[pygame.K_a] or lKeys[pygame.K_LEFT]: #left
		print("left")
		gDirection="left"
	if lKeys[pygame.K_d] or lKeys[pygame.K_RIGHT]: #right
		print("right")
		gDirection="right"

	# move the snake (grow in direction), into last (or changed) direction
	if gDirection=="up":
		gSnakePositions.insert(0, pygame.Vector2(gSnakePositions[0].x, gSnakePositions[0].y-gRectangleSize))
	elif gDirection=="down":
		gSnakePositions.insert(0, pygame.Vector2(gSnakePositions[0].x, gSnakePositions[0].y+gRectangleSize))
	elif gDirection=="left":
		gSnakePositions.insert(0, pygame.Vector2(gSnakePositions[0].x-gRectangleSize, gSnakePositions[0].y))
	elif gDirection=="right":
		gSnakePositions.insert(0, pygame.Vector2(gSnakePositions[0].x+gRectangleSize, gSnakePositions[0].y))

	# Remove last element
	if gPowerpillCounter==0:
#		print("Popping")
		gSnakePositions.pop()
	else:
		gPowerpillCounter-=1
		# dont pop, let snake grow

	# fill the screen with a color to wipe away anything from last frame
	gScreen.fill(gColorBackground)

	# Draw Powerpill
	gPowerpillPositionTemp=pygame.Vector2(gPowerpillPosition.x+gRectangleSize/2, gPowerpillPosition.y+gRectangleSize/2)
	pygame.draw.circle(gScreen, "blue", gPowerpillPositionTemp, gRectangleSize/2/2)

	# Draw snake
	for lI in range(len(gSnakePositions)):
		#print("Drawing #" + str(lI) + " ( "+ str(gSnakeXPositions[lI]) + "/)" + str(gSnakeYPositions[lI]))
		pygame.draw.rect(gScreen, "red", pygame.Rect(gSnakePositions[lI].x, gSnakePositions[lI].y, gRectangleSize, gRectangleSize))

	# now print the score
	printScore()

	# flip() the display to put your work on screen
	pygame.display.flip()

	# Check Border hit
	if gSnakePositions[0].x < 0 or gSnakePositions[0].x > gScreenSizeX - gRectangleSize or gSnakePositions[0].y < 0 or gSnakePositions[0].y > gScreenSizeY-gRectangleSize:
		print("BANG!")
		#gRunning = False
		wait()

# Check powerpill-hit
#	if (abs(gSnakeXPositions[0]-gPowerpillPosition.x) <= gRectangleSize/2) and (abs(gSnakeYPositions[0]-gPowerpillPosition.y) <= gRectangleSize/2):
	print(str(gSnakePositions[0].x) + "/" + str(gSnakePositions[0].y))
	if gSnakePositions[0].x==gPowerpillPosition.x and gSnakePositions[0].y==gPowerpillPosition.y:
		print("Hit powerpill!")
		gPowerpillPosition=pygame.Vector2(random.randrange(0,gTilesX-1)*gRectangleSize-1, random.randrange(1,gTilesY-1)*gRectangleSize-1)
		gPowerpillCounter=2 # rects to add to snake
		print("gPowerpillPosition: " + str(gPowerpillPosition))
		gScore=gScore+gPowerpillCounter

	gClock.tick(2)  # limit FPS

# Ende & Ergebnis
#wait()
#printScore()

# The End
#pygame.quit()

# Ende
