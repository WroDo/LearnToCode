import pygame
import random
from commonStrings import * # create symbolic link to access commonStrings.py
from commonPygame import * # create symbolic link to access commonStrings.py

# globals
pygame.init()
gScreenSizeX=640;
gScreenSizeY=480;
gRunning = True
gColorBackground="black"
gColorBorder="white"
gColorText="white"
gFontSize=36
gText = ""
gTextMaxLen=3

# pygame setup
gScreen = pygame.display.set_mode((gScreenSizeX, gScreenSizeY))
gClock = pygame.time.Clock()
gFont = pygame.font.Font(pygame.font.get_default_font(), gFontSize)

# Functions
def drawText():
    global gScreen, gScreenSizeX, gScreenSizeY, gFontSize, gFont, gColorText
    lTextSurface = gFont.render(str(gText), True, gColorText)
    gScreen.blit(lTextSurface, dest=(gScreenSizeX/2-(lTextSurface.get_width() /2), gFontSize))

# Main
while gRunning:
    # Poll events, if exist
    for lEvent in pygame.event.get():
        if lEvent.type == pygame.QUIT:
            print("QUIT")
            gRunning=False
            #pygame.quit()
        if lEvent.type == pygame.KEYDOWN:
            gText=appendCharToStringFromEvent(lEvent, gText, 3, "###QUIT###")
            if gText=="###QUIT###":
                gRunning=False

    # fill the screen with a color to wipe away anything from last frame
    gScreen.fill(gColorBackground)

    # now print the text
    drawText()

    # flip() the display to put your work on screen
    pygame.display.flip()

    gClock.tick(30)  # limit FPS
    print("Turnover!")
# End of main loop

pygame.quit()

print("gText: " + gText)

# Ende
