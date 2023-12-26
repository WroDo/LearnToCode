import pygame
import random

pygame.init()
gScreenSizeX=1040
gScreenSizeY=880
gRunning = True
gColorBackground="white"
gColorBall="black"
gColorBorder="red"
gColorText="white"
gBallSize=5
gBallSpeedMin=5
gBallSpeedMax=8

gBallPosition=pygame.Vector2(0,0)
gBallDirection=pygame.Vector2(0,0)


gScreen = pygame.display.set_mode((gScreenSizeX, gScreenSizeY))
gClock = pygame.time.Clock()


def randomizeBall():
	global gBallDirection, gBallPosition, gBallSpeedMax, gScreenSizeX, gScreenSizeY
	gBallPosition=pygame.Vector2(int(gScreenSizeX/2), int(gScreenSizeY/2))
	gBallDirection=pygame.Vector2(int(random.randrange(gBallSpeedMin,gBallSpeedMax)), int(random.randrange(gBallSpeedMin,gBallSpeedMax)))
	if round(random.randrange(0,2)) == 0:
		gBallDirection.x=-gBallDirection.x
	if round(random.randrange(0,2)) == 0:
		gBallDirection.y=-gBallDirection.y

randomizeBall()


while gRunning == True:
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
			gRunning = False


    # Move ball
	gBallPosition=gBallPosition+gBallDirection
    
    # Hits of vertical bounderies
	if gBallPosition.y <= gBallSize/2 or gBallPosition.y >= gScreenSizeY-gBallSize/2:
		gBallDirection.y=-gBallDirection.y
    
    
    # Hits of horizontal bounderies
	if gBallPosition.x <= gBallSize/2 or gBallPosition.x >= gScreenSizeX-gBallSize/2:
		# Count scores
		randomizeBall()


	gScreen.fill(gColorBackground)

	# Draw vertical borders
	pygame.draw.line(gScreen, gColorBorder, pygame.Vector2(0, 0), pygame.Vector2(gScreenSizeX-1, 0), 1)
	pygame.draw.line(gScreen, gColorBorder, pygame.Vector2(0, gScreenSizeY-1), pygame.Vector2(gScreenSizeX-1, gScreenSizeY-1), 1)

	# Draw Ball
	pygame.draw.circle(gScreen, gColorBall, gBallPosition, gBallSize)

	# Draw paddles
#	pygame.draw.rect(gScreen, gPaddleColor, pygame.Rect( gPaddleLeftPosition.x, gPaddleLeftPosition.y,  gPaddleWidth, gPaddleHeight))
#	pygame.draw.rect(gScreen, gPaddleColor, pygame.Rect(gPaddleRightPosition.x, gPaddleRightPosition.y, gPaddleWidth, gPaddleHeight))

	# now print the scores
#	lTextSurface = gFont.render(str(gScoreLeft)+" : "+str(gScoreRight), True, gColorText)
#	gScreen.blit(lTextSurface, dest=(gScreenSizeX/2-(lTextSurface.get_width() /2), gFontSize))

	# flip() the display to put your work on screen
	pygame.display.flip()

	gClock.tick(25)  # limit FPS

pygame.quit()

