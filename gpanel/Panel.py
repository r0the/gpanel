import tkinter
from .Element import Element
from .Circle import Circle
from .Line import Line
from .Rectangle import Rectangle
from .EventHandler import EventHandler

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
        dx = maxx - minx
        dy = miny - maxy
        self._minx = minx
        self._miny = miny
        self._scalex = self._width / dx
        self._scaley = self._height / dy

    @property
    def background(self):
        return self._canvas["background"]

    @background.setter
    def background(self, value):
        self._canvas.config(background=value)

    def bind(self, event, handler):
        if not event in self._events:
            self_events[event] = []
        self._events[event].append(handler)

    def color(self, value):
        self._fillcolor = value
        self._pencolor = value

    def fillcolor(self, value):
        self._fillcolor = value

    def pencolor(self, value):
        self._pencolor = value

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
        return (x - self._minx) * self._scalex

    def _py(self, y):
        return self._height - (self._miny - y) * self._scaley
