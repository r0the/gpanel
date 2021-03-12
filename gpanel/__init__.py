from .Element import Element
from .Circle import Circle
from .Panel import Panel
from time import sleep

__global_panel = None

def create_gpanel(*args):
    global __global_panel
    width = 600
    height = 600
    if len(args) == 2:
        width = args[0]
        height = args[1]
    result = Panel(width, height)
    if not __global_panel:
        __global_panel = result
    return result

def __gp():
    global __global_panel
    if not __global_panel:
        create_gpanel()
    return __global_panel

def coordinates(minx, miny, maxx, maxy):
    __gp().coordinates(minx, miny, maxx, maxy)

def circle(x, y, radius):
    __gp().circle(x, y, radius)

def pencolor(c):
    __gp().pencolor(c)

def fillcolor(c):
    __gp().fillcolor(c)

def color(c):
    __gp().color(c)

def line(x1, y1, x2, y2):
    __gp().line(x1, y1, x2, y2)

def rectangle(x1, y1, x2, y2):
    __gp().rectangle(x1, y1, x2, y2)

def event(handler):
    __gp().bind(handler)
