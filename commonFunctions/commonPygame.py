# All about pygame helpers

from commonStrings import *

def appendCharToStringFromEvent(aEvent, aText, aMaxLen, aQuitString): # feed it a key-event and let it handle it
    #global gText, gRunning
    lEventKeyString=""
    lEventKeyOrd=aEvent.key
    lText=aText
    if (lEventKeyOrd >= 97 and lEventKeyOrd <= 122):
        lEventKeyOrd=lEventKeyOrd-32
    if (lEventKeyOrd >= 64 and lEventKeyOrd <= 90):
        lEventKeyString=chr(lEventKeyOrd)
    print("KEYDOWN: (" + str(aEvent.key) + "/" + str(lEventKeyOrd) + ")")
    if lEventKeyOrd == 8: # Backspace
        lText=lText[:-1]
    if lEventKeyOrd == 13: # Return
        lText=aQuitString
        #gRunning=False
    else:
        if len(lText) == aMaxLen:
            lText=shiftStringLeft(lText, 1)
        lText=lText+lEventKeyString
    return(lText)
