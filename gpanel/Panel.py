import tkinter
from .Element import Element
from .Circle import Circle
from .Line import Line
from .Rectangle import Rectangle
from .EventHandler import EventHandler
from .Rect import Rect

def rgbtohex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def convert_color(arg):
    if isinstance(arg, tuple):
         return rgbtohex(arg[0], arg[1], arg[2])
    return arg

class Panel:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.coordinates(0.0, 0.0, 1.0, 1.0)
        self._root = tkinter.Tk()
        self._canvas = tkinter.Canvas(self._root, width=width, height=height)
        self._canvas.pack()
        self._handler = EventHandler()
        self._fillcolor = "black"
        self._pencolor = "black"
        self._canvas.bind("<Motion>", self._motion)

    def _motion(self, event):
        self._handler.on_mouse_move(self, self._px(event.x), self._py(event.y))

    def coordinates(self, minx, miny, maxx, maxy):
        self._bounds = Rect(minx, miny, maxx - minx, maxy - miny)

    @property
    def background(self):
        return self._canvas["background"]

    @background.setter
    def background(self, value):
        self._canvas.config(background=value)

    def bounds(self):
        return self._bounds

    def bind(self, handler):
        self._handler(handler)

    def color(self, *args):
        self._fillcolor = convert_color(args)
        self._pencolor = convert_color(args)

    def fillcolor(self, *args):
        self._fillcolor = convert_color(args)

    def pencolor(self, *args):
        self._pencolor = convert_color(args)

    def circle(self, x, y, radius):
        return Circle(self, x, y, radius)

    def line(self, x1, y1, x2, y2):
        return Line(self, x1, y1, x2, y2)

    def rectangle(self, x1, y1, x2, y2):
        return Rectangle(self, x1, y1, x2, y2)

    def start(self):
        self._root.mainloop()

    def update(self):
        self._canvas.update()

    def _p(self, points):
        result = []
        for p in points:
            result.append(self._px(p[0]))
            result.append(self._py(p[1]))
        return result

    def _px(self, x):
        b = self._bounds
        return (x - b.left) * (self._width / b.width)

    def _py(self, y):
        b = self._bounds
        return self._height - (y - b.bottom) * (self._height / b.height)
