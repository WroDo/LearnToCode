import pygame
import random

# globals
pygame.init()
gScreenSizeX=640
gScreenSizeY=480
gRunning = True
gColorBackground="white"
gColorText="white"
gFontSize=36
gFont = pygame.font.Font(pygame.font.get_default_font(), gFontSize)
gScoreLeft=0
gScoreRight=0
gCloudCount=3
gCloudPositions=list()
gCloudSpeeds=list()
gCloudSpeedMin=1
gCloudSpeedMax=5
gGroundImageSizeY=gScreenSizeY*2
gGroundImagePosition=pygame.Vector2(0, -(gGroundImageSizeY-gScreenSizeY))
gGroundImageSpeed=1
gShip01Position=pygame.Vector2(int(gScreenSizeX/2), int(gScreenSizeY/2))
gShipSpeed=5
gShots01Positions=list()
gShotSize=5
gShotColor='red'
gShotSpeed=5
gShot01Deadband=0
gShot01Rate=5 #how much frames must pass before new shot can be fired
gTargetCount=5 # how much should be on-screen at any time
gTargetPositions=list()
gTargetSpeeds=list()
gTargetSpeedMin=2
gTargetSpeedMax=5

# pygame setup
gScreen = pygame.display.set_mode((gScreenSizeX, gScreenSizeY))
gClock = pygame.time.Clock()

# Load resources - clouds
gCloudImageFiles = [ 'images/cloud01.png' ]
gCloudImages = list()
for lCloudImageFile in gCloudImageFiles:
	gCloudImages.append(pygame.image.load(lCloudImageFile))
# Load resources - targets
gTargetImageFiles = [ 'images/target01.png' ]
gTargetImages = list()
for lTargetImageFile in gTargetImageFiles:
	gTargetImages.append(pygame.image.load(lTargetImageFile))

# Init Clouds-Positions
for lI in range(gCloudCount):
	gCloudPositions.append(pygame.Vector2(int(random.randrange(0,gScreenSizeX-100)), -100))
	gCloudSpeeds.append(int(random.randrange(gCloudSpeedMin, gCloudSpeedMax)))

# Init Target-Positions
for lI in range(gTargetCount):
	gTargetPositions.append(pygame.Vector2(int(random.randrange(0,gScreenSizeX-100)), -100))
	gTargetSpeeds.append(pygame.Vector2(int(random.randrange(gTargetSpeedMin, gTargetSpeedMax)), int(random.randrange(gTargetSpeedMin, gTargetSpeedMax)) ) )

# Create ground image
gGroundImage=pygame.image.load('images/ground01.png')

# Load Ships Images
gShip01Image=pygame.image.load('images/ship01.png')


# Main
while gRunning:
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
			gRunning = False

	# Move ground
	gGroundImagePosition.y = gGroundImagePosition.y + gGroundImageSpeed
	if gGroundImagePosition.y >= 0:
		gGroundImagePosition=pygame.Vector2(0, -(gGroundImageSizeY-gScreenSizeY))

	# Move clouds
	for lI in range(gCloudCount):
		# Move down
		gCloudPositions[lI].y = gCloudPositions[lI].y + gCloudSpeeds[lI]
		# am unteren Rand vorbei?
		if gCloudPositions[lI].y > gScreenSizeY:
			gCloudPositions[lI]=pygame.Vector2(int(random.randrange(0,gScreenSizeX-100)), -300) # TODO USE REAL IMAGE SIZE FOR -Y OFFSET

	# Move targets
	for lI in range(gTargetCount):
		# Move down
		gTargetPositions[lI] = gTargetPositions[lI] + gTargetSpeeds[lI]
		# am unteren Rand vorbei?
		if gTargetPositions[lI].y > gScreenSizeY or gTargetPositions[lI].x > gScreenSizeX:
			gTargetPositions[lI]=pygame.Vector2(int(random.randrange(0, gScreenSizeX-100)), -300) # TODO USE REAL IMAGE SIZE FOR -Y OFFSET
			gTargetSpeeds[lI]=pygame.Vector2(int(random.randrange(gTargetSpeedMin, gTargetSpeedMax)), int(random.randrange(gTargetSpeedMin, gTargetSpeedMax)) )

	# Move shots
	for lShot in gShots01Positions:
		lShot.y=lShot.y-gShotSpeed
	
	# Limit shot range
	lShots01Positions=list()
	for lShot in gShots01Positions:
		if lShot.y <= 0:
			print("out!")
		else:
			lShots01Positions.append(lShot)
	gShots01Positions=lShots01Positions
	
	# Limit shot count
	if gShot01Deadband >0:
		gShot01Deadband=gShot01Deadband-1
	
	# Read keyboard event and set coordinates of head (new rect). Key-Constants: https://www.pygame.org/docs/ref/key.html
	lKeys = pygame.key.get_pressed()
	# Player 01
	if lKeys[pygame.K_UP]:
		print("01 up")
		gShip01Position.y=gShip01Position.y-gShipSpeed
	if lKeys[pygame.K_DOWN]:
		print("01 down")
		gShip01Position.y=gShip01Position.y+gShipSpeed
	if lKeys[pygame.K_LEFT]:
		print("01 left")
		gShip01Position.x=gShip01Position.x-gShipSpeed
	if lKeys[pygame.K_RIGHT]:
		print("01 right")
		gShip01Position.x=gShip01Position.x+gShipSpeed
	if lKeys[pygame.K_SPACE] and gShot01Deadband==0:
		print("01 shot")
		gShots01Positions.append(pygame.Vector2(gShip01Position.x+40-4, gShip01Position.y)) #TODO USE ACTUAL SHIP DIMENSION
		gShot01Deadband=gShot01Rate

	# Limit movement of ship(s)
	if gShip01Position.y < 0:
		gShip01Position.y=0
	if gShip01Position.y > gScreenSizeY:
		gShip01Position.y=gScreenSizeY
	if gShip01Position.y < 0:
		gShip01Position.y=0
	if gShip01Position.y > gScreenSizeY:
		gShip01Position.y=gScreenSizeY

	# fill the screen with a color to wipe away anything from last frame
	gScreen.fill(gColorBackground)

	# draw ground
	gScreen.blit(gGroundImage, dest=gGroundImagePosition)

	# draw the clouds
	for lI in range(gCloudCount):
		gScreen.blit(gCloudImages[0], dest=gCloudPositions[lI])

	# draw the targets
	for lI in range(gTargetCount):
		gScreen.blit(gTargetImages[0], dest=gTargetPositions[lI])
	
	# Draw ship(s)
	gScreen.blit(gShip01Image, dest=gShip01Position)

	# Draw shots
	for lShot in gShots01Positions:
		pygame.draw.circle(gScreen, gShotColor, lShot, gShotSize)

	# now print the scores
#	lTextSurface = gFont.render(str(gScoreLeft)+" : "+str(gScoreRight), True, gColorText)
#	gScreen.blit(lTextSurface, dest=(gScreenSizeX/2-(lTextSurface.get_width() /2), gFontSize))

	# flip() the display to put your work on screen
	pygame.display.flip()

	gClock.tick(25)  # limit FPS


# The End
pygame.quit()




# Ende
