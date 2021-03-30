from random import *
from turtle import *
import os

def path(filename):
    "Return full path to `filename` in freegames module."
    filepath = os.path.realpath(__file__)
    dirpath = os.path.dirname(filepath)
    fullpath = os.path.join(dirpath, 'images', filename)
    return fullpath

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('white', 'black')
    begin_fill()
    for count in range(4):
        forward(100)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 100 + ((y + 200) // 100) * 4)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 4) * 100 - 200, (count // 4) * 100 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(image)
    stamp()

    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('white')
        write(tiles[mark], font=('Arial', 60, 'normal'))

    update()
    ontimer(draw, 100)


imageList = ["123.gif", "456.gif", "789.gif", "car.gif"]
image = path(choice(imageList))
tiles = list(range(8)) * 2
state = {'mark': None}
hide = [True] * 16


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(image)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
