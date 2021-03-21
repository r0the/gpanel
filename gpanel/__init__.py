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

def bounds():
    return __gp().bounds()

def circle(x, y, radius):
    return __gp().circle(x, y, radius)

def pencolor(*args):
    __gp().pencolor(*args)

def fillcolor(*args):
    __gp().fillcolor(*args)

def color(*args):
    __gp().color(*args)

def line(x1, y1, x2, y2):
    return __gp().line(x1, y1, x2, y2)

def rectangle(x, y, width, height):
    return __gp().rectangle(x, y, width, height)

def event(handler):
    __gp().bind(handler)

