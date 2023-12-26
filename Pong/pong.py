# Nah: https://docs.python.org/3/howto/curses.html
# Yeah: https://www.pygame.org/docs/

import pygame
import random

# globals
pygame.init()
gScreenSizeX=640
gScreenSizeY=480
gRunning = True
gColorBackground="black"
gColorBall="white"
gColorBorder="white"
gColorText="white"
gBallSize=5
gBallSpeedMin=4
gBallSpeedMax=8
gFontSize=36
gFont = pygame.font.Font(pygame.font.get_default_font(), gFontSize)
gScoreLeft=0
gScoreRight=0
gBallPosition=pygame.Vector2(0,0)
gBallDirection=pygame.Vector2(0,0)
gPaddleHeight=42+23
gPaddleWidth=10
gPaddleLeftPosition=pygame.Vector2(0, int(gScreenSizeY/2)-1) # coordinates for top-left corner
gPaddleRightPosition=pygame.Vector2(gScreenSizeX-gPaddleWidth, int(gScreenSizeY/2)-1) # coordinates for top-left corner
gPaddleStep=10
gPaddleColor="white"

# pygame setup
gScreen = pygame.display.set_mode((gScreenSizeX, gScreenSizeY))
gClock = pygame.time.Clock()

# Functions
def randomizeBall():
	global gBallDirection, gBallPosition, gBallSpeedMax, gScreenSizeX, gScreenSizeY
	gBallPosition=pygame.Vector2(int(gScreenSizeX/2), int(gScreenSizeY/2))
	gBallDirection=pygame.Vector2(int(random.randrange(gBallSpeedMin,gBallSpeedMax)), int(random.randrange(gBallSpeedMin,gBallSpeedMax)))
	if round(random.randrange(0,2)) == 0:
		gBallDirection.x=-gBallDirection.x
	if round(random.randrange(0,2)) == 0:
		gBallDirection.y=-gBallDirection.y

# Main
randomizeBall()
print("gBallPosition: " + str(gBallPosition))
while gRunning:
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
			gRunning = False

	# Read keyboard event and set coordinates of head (new rect). Key-Constants: https://www.pygame.org/docs/ref/key.html
	lKeys = pygame.key.get_pressed()
	# Left Player
	if lKeys[pygame.K_a]: #up
		print("left up")
		gPaddleLeftPosition.y=gPaddleLeftPosition.y-gPaddleStep
	if lKeys[pygame.K_y]: #down
		print("left down")
		gPaddleLeftPosition.y=gPaddleLeftPosition.y+gPaddleStep
	# Right Player
	if lKeys[pygame.K_w] or lKeys[pygame.K_UP]: #up
		print("right up")
		gPaddleRightPosition.y=gPaddleRightPosition.y-gPaddleStep
	if lKeys[pygame.K_s] or lKeys[pygame.K_DOWN]: #down
		print("right down")
		gPaddleRightPosition.y=gPaddleRightPosition.y+gPaddleStep

	# Limit movement
	if gPaddleLeftPosition.y < 0:
		gPaddleLeftPosition.y=0
	if gPaddleLeftPosition.y > gScreenSizeY-gPaddleHeight:
		gPaddleLeftPosition.y=gScreenSizeY-gPaddleHeight
	if gPaddleRightPosition.y < 0:
		gPaddleRightPosition.y=0
	if gPaddleRightPosition.y > gScreenSizeY-gPaddleHeight:
		gPaddleRightPosition.y=gScreenSizeY-gPaddleHeight

	# Move ball
	gBallPosition=gBallPosition+gBallDirection

	# Hits of vertical bounderies
	if gBallPosition.y <= gBallSize/2 or gBallPosition.y >= gScreenSizeY-gBallSize/2:
		gBallDirection.y=-gBallDirection.y

	# Hits of horizontal bounderies
	if gBallPosition.x <= gBallSize/2 or gBallPosition.x >= gScreenSizeX-gBallSize/2:
		# Count scores
		if gBallPosition.x <= gBallSize/2:
			gScoreRight+=1
		else:
			gScoreLeft+=1
		# New ball
		randomizeBall()

	# Check Paddle-Ball-Hit
	if gBallPosition.x <= gPaddleLeftPosition.x+gPaddleWidth and gBallPosition.y >=gPaddleLeftPosition.y and gBallPosition.y < gPaddleLeftPosition.y+gPaddleHeight:
		print("Hit left paddle")
		gBallDirection.x=-gBallDirection.x
	if gBallPosition.x >= gPaddleRightPosition.x and gBallPosition.y >=gPaddleRightPosition.y and gBallPosition.y < gPaddleRightPosition.y+gPaddleHeight:
		print("Hit right paddle")
		gBallDirection.x=-gBallDirection.x

	# fill the screen with a color to wipe away anything from last frame
	gScreen.fill(gColorBackground)

	# Draw vertical borders
	pygame.draw.line(gScreen, gColorBorder, pygame.Vector2(0, 0), pygame.Vector2(gScreenSizeX-1, 0), 1)
	pygame.draw.line(gScreen, gColorBorder, pygame.Vector2(0, gScreenSizeY-1), pygame.Vector2(gScreenSizeX-1, gScreenSizeY-1), 1)

	# Draw Ball
	pygame.draw.circle(gScreen, gColorBall, gBallPosition, gBallSize)

	# Draw paddles
	pygame.draw.rect(gScreen, gPaddleColor, pygame.Rect( gPaddleLeftPosition.x, gPaddleLeftPosition.y,  gPaddleWidth, gPaddleHeight))
	pygame.draw.rect(gScreen, gPaddleColor, pygame.Rect(gPaddleRightPosition.x, gPaddleRightPosition.y, gPaddleWidth, gPaddleHeight))

	# now print the scores
	lTextSurface = gFont.render(str(gScoreLeft)+" : "+str(gScoreRight), True, gColorText)
	gScreen.blit(lTextSurface, dest=(gScreenSizeX/2-(lTextSurface.get_width() /2), gFontSize))

	# flip() the display to put your work on screen
	pygame.display.flip()

	gClock.tick(25)  # limit FPS


# The End
pygame.quit()




# Ende
