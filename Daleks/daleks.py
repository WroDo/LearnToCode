import pygame
import random
import time
import copy

# globals
pygame.init()
gScreenSizeX=640
gScreenSizeY=480
gTileSize=40
gTilesX=gScreenSizeX/gTileSize
gTilesY=gScreenSizeY/gTileSize
gRunning = True
gColorBackground="white"
gColorText="white"
gColorGrid="grey"
gFontSize=36
gFont = pygame.font.Font(pygame.font.get_default_font(), gFontSize)
gScoreLeft=0
gDalekCount=5 # how much should be on-screen at start #TODO: Limit to tile-count...
gDalekPositions=list()
gDalekPositionsExterminated=list()
gSonicScrewdriversCount=1

# pygame setup
gScreen = pygame.display.set_mode((gScreenSizeX, gScreenSizeY))
gClock = pygame.time.Clock()

# Load resources
gDalekImage=pygame.image.load('images/dalek_38px.png')
gDalekImageExterminated=pygame.image.load('images/dalek_exterminated_38px.png')
gPlayerImage=pygame.image.load('images/tardis_38px.png')
gSonicScrewdriverImage=pygame.image.load('images/sonic_screwdriver_38px.png')
gTeleportImage=pygame.image.load('images/teleport_38px.png')

#def calculateUnusedPosition():
#	while 
#	lPosition=pygame.Vector2(int(random.randrange(0,gTilesX-1)), int(random.randrange(0,gTilesY-1))

def isPositionEqual(aPosition1, aPosition2):
	if aPosition1.x == aPosition2.x and aPosition1.y == aPosition2.y:
		return True
	else:
		return False

def positionIsUsed(aPos):
	global gDalekPositions, gDalekPositionsExterminated, gPlayerPosition
	print("positionIsUsed.aPos: " + str(aPos))
	lReturnValue=False
	if aPos.x == gPlayerPosition.x and aPos.y == gPlayerPosition.y:
		lReturnValue=True
	for lDalekPosition in gDalekPositions:
		if aPos.x == lDalekPosition.x and aPos.y == lDalekPosition.y:
			lReturnValue=True
	for lDalekPosition in gDalekPositionsExterminated:
		if aPos.x == lDalekPosition.x and aPos.y == lDalekPosition.y:
			lReturnValue=True
	print("lReturnValue: " + str(lReturnValue))
	return lReturnValue

def playerCanMoveTo(aPos):
	global gDalekPositionsExterminated, gPlayerPosition, gTilesX, gTilesY # gDalekPositions
	print("playerCanMoveTo.aPos: " + str(aPos))
	lReturnValue=True
	if aPos.x < 0 or aPos.x >= gTilesX or aPos.y < 0 or aPos.y >= gTilesY:
		lReturnValue=False
	for lDalekPosition in gDalekPositionsExterminated:
		if isPositionEqual(aPos, lDalekPosition):
			lReturnValue=False
	print("lReturnValue: " + str(lReturnValue))
	return lReturnValue

# Init Player Position
gPlayerPosition=pygame.Vector2(int(random.randrange(0, int(gTilesX-1) )), int(random.randrange(0, int(gTilesY-1) )))
	
# Init Dalek-Positions
for lI in range(gDalekCount):
	#lPos=pygame.Vector2(int(random.randrange(0,gTilesX-1)), int(random.randrange(0,gTilesY-1))
	while positionIsUsed(lPos:=pygame.Vector2(int(random.randrange(int(0), int(gTilesX-1))), int(random.randrange(int(0), int(gTilesY-1))))):
		print("Oops.")
	gDalekPositions.append(lPos)


def sonic():
	global gDalekPositions, gDalekPositionsExterminated, gPlayerPosition, gSonicScrewdriversCount
	print('Sonic player: ' + str(gPlayerPosition))
	gSonicScrewdriversCount=gSonicScrewdriversCount-1
	if gSonicScrewdriversCount>=0:
		for lDalekPosition in gDalekPositions:
			if abs(lDalekPosition.x - gPlayerPosition.x)==1:
				gDalekPositionsExterminated.append(lDalekPosition)
				gDalekPositions.remove(lDalekPosition)
				print('Sonic dalek (x): ' + str(lDalekPosition))
		for lDalekPosition in gDalekPositions:
			if abs(lDalekPosition.y - gPlayerPosition.y)==1:
				gDalekPositionsExterminated.append(lDalekPosition)
				gDalekPositions.remove(lDalekPosition)
				print('Sonic dalek (y): ' + str(lDalekPosition))
	else:
		print('No screwdrivers left');


def drawPlayingField():
	global gScreen, gColorBackground, gPlayerPosition, gTileSize, gPlayerImage, gDalekImage, gDalekImageExterminated, gSonicScrewdriverImage, gTeleportImage, gColorGrid
	print("Draw!")
	
	# Erase
	gScreen.fill(gColorBackground)

	# Draw Grid
	for lX in range(0, gScreenSizeX, gTileSize):
		lUpperPosition=pygame.Vector2(lX, 0)
		lLowerPosition=pygame.Vector2(lX, gScreenSizeY-1)
		pygame.draw.line(gScreen, gColorGrid, lUpperPosition, lLowerPosition)
	for lY in range(0, gScreenSizeX, gTileSize):
		lLeftPosition=pygame.Vector2(0, lY)
		lRightPosition=pygame.Vector2(gScreenSizeX-1, lY)
		pygame.draw.line(gScreen, gColorGrid, lLeftPosition, lRightPosition)
	
	# Draw Player
	lPlayerPosition=pygame.Vector2(gPlayerPosition.x*gTileSize, gPlayerPosition.y*gTileSize)
	gScreen.blit(gPlayerImage, dest=lPlayerPosition)

	# Draw living Daleks
	for lDalekPosition in gDalekPositions:
		lDalekPosition=pygame.Vector2(lDalekPosition.x*gTileSize, lDalekPosition.y*gTileSize)
		gScreen.blit(gDalekImage, dest=lDalekPosition)
		
	# Draw exterminated Daleks
	for lDalekPosition in gDalekPositionsExterminated:
		lDalekPosition=pygame.Vector2(lDalekPosition.x*gTileSize, lDalekPosition.y*gTileSize)
		gScreen.blit(gDalekImageExterminated, dest=lDalekPosition)

	# flip() the display to put your work on screen
	pygame.display.flip()
	#gClock.tick(30)  # limit FPS
# END OF drawPlayingField()

# Main
time.sleep(0.1) # w/o first draw fails
drawPlayingField()
while gRunning:
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
			gRunning = False
		if event.type == pygame.KEYDOWN:
			# Read keyboard event and set coordinates of head (new rect). Key-Constants: https://www.pygame.org/docs/ref/key.html
			lKeys = pygame.key.get_pressed()
			# Player 01
			lPlayerPositionBackup=copy.deepcopy(gPlayerPosition)
			if lKeys[pygame.K_UP]:
				print("01 up")
				gPlayerPosition.y=gPlayerPosition.y-1
			if lKeys[pygame.K_DOWN]:
				print("01 down")
				gPlayerPosition.y=gPlayerPosition.y+1
			if lKeys[pygame.K_LEFT]:
				print("01 left")
				gPlayerPosition.x=gPlayerPosition.x-1
			if lKeys[pygame.K_RIGHT]:
				print("01 right")
				gPlayerPosition.x=gPlayerPosition.x+1
			if lKeys[pygame.K_SPACE or pygame.K_s]:
				print("01 sonic the adjacent daleks")
				sonic()
			if lKeys[pygame.K_t]:
				print("01 teleport with tardis")


			# Limit movement of player #TODO use playerCanMoveTo()
			if not playerCanMoveTo(gPlayerPosition):
				gPlayerPosition=copy.deepcopy(lPlayerPositionBackup)
#			if gPlayerPosition.y < 0:
#				gPlayerPosition.y=0
#			if gPlayerPosition.y >= gTilesY:
#				gPlayerPosition.y=gTilesY-1
#			if gPlayerPosition.x < 0:
#				gPlayerPosition.x=0
#			if gPlayerPosition.x >= gTilesX:
#				gPlayerPosition.x=gTilesX-1
				
			# Move Daleks
			for lDalekPosition in gDalekPositions:
				if lDalekPosition.x > gPlayerPosition.x:
					lDalekPosition.x = lDalekPosition.x - 1
				if lDalekPosition.x < gPlayerPosition.x:
					lDalekPosition.x = lDalekPosition.x + 1
				if lDalekPosition.y > gPlayerPosition.y:
					lDalekPosition.y = lDalekPosition.y - 1
				if lDalekPosition.y < gPlayerPosition.y:
					lDalekPosition.y = lDalekPosition.y + 1
			
			# Check Collision of (living) Daleks
			l1=-1
			l2=-1
			for lDalekPosition1 in gDalekPositions:
				l1=l1+1
				for lDalekPosition2 in gDalekPositions:
					l2=l2+1
#					if (lDalekPosition1!=lDalekPosition2 and isPositionEqual(lDalekPosition1, lDalekPosition2)):
					if (l1!=l2 and isPositionEqual(lDalekPosition1, lDalekPosition2)):
						gDalekPositionsExterminated.append(lDalekPosition1)
						gDalekPositions.remove(lDalekPosition1)
						print("This Daleks collided: " + str(lDalekPosition1) + "(" + str(l1) + ")" + str(lDalekPosition2) + "(" + str(l2) + ")")
				l2=-1
			
			# Check Collision of (living and exterminated) Daleks
			for lDalekPosition1 in gDalekPositions:
				for lDalekPosition2 in gDalekPositionsExterminated:
					if (isPositionEqual(lDalekPosition1, lDalekPosition2)):
						gDalekPositions.remove(lDalekPosition1)
						print("This Dalek (1) collided with exterminated dalek (2): " + str(lDalekPosition1) + str(lDalekPosition2) )

			
			# Check Collision with The Doctor
			for lDalekPosition in gDalekPositions:
					if (isPositionEqual(lDalekPosition, gPlayerPosition)):
						print("GAME OVER")


			# Draw!
			drawPlayingField()


	gClock.tick(30)  # limit FPS

# The End
pygame.quit()




# Ende
