from PIL import ImageGrab, ImageOps
import        , time
from numpy import *

class Cordinates ():
    replayBtn = (960,450)
    dino      = (666,460)


def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("JUMP")
    pyautogui.keyUp('space')

def imgGrab ():
    box = (Cordinates.dino[0]+100,Cordinates.dino[1],Cordinates.dino[0]+140,Cordinates.dino[1]+20 )
    image = ImageGrab.grab(box)
    grayImage  =ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return (a.sum())

def main () :
    restartGame()
    while True_:
        if(imgGrab ()!= 1047):
            pressSpace()
            time.sleep(0.1)
main()

# while True:
#     imgGrab()