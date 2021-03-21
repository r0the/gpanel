from gpanel import *
from random import randrange

coordinates(0, 0, 100, 100)

for i in range(80):
    x = randrange(0, 100)
    y = randrange(0, 100)
    width = randrange(10, 30)
    height = randrange(5, 30)
    color(randrange(0, 256), randrange(0, 256), randrange(0, 246))
    rectangle(x, y, width, height) 
