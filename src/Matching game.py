from random import *
from turtle import *
import images.LoadImages
import os

def path(imageName):
    filePath = os.path.realpath(__file__)
    directoryPath = os.path.dirname(filePath)
    fullPath = os.path.join(directoryPath, 'images', imageName)
    return fullPath

def paintSquare(x, y):
    up()
    goto(x, y)
    down()
    color('white', 'dimgray')
    begin_fill()
    for count in range(4):
        forward(150)
        left(90)
    end_fill()

def index(x, y):
    return int((x + 450) // 150 + ((y + 450) // 150) * 6)

def location(count):
    return (count % 6) * 150 - 450, (count // 6) * 150 - 450

def leftClick(x, y):
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        if all(x == hide[0] for x in hide):
            print("You win!")
            print("If you want to play again, please restart the game.")
        
def paint():
    clear()
    goto(0, 0)
    shape(image)
    stamp()

    for count in range(36):
        if hide[count]:
            x, y = location(count)
            paintSquare(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = location(mark)
        up()
        goto(x + 2, y)
        color('white')
        write(tiles[mark]+1, font=('Arial', 90))

    update()
    ontimer(paint, 100)

######################################

setup(920, 920, 300, 30)
title("Matching game")
tiles = list(range(18)) * 2
state = {'mark': None}
hide = [True] * 36
shuffle(tiles)
hideturtle()
tracer(False)
imageList = images.LoadImages.loadImages()
image = path(choice(imageList))
addshape(image)
onscreenclick(leftClick)
paint()
done()
