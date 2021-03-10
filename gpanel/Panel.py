import tkinter
from .Element import Element
from .Circle import Circle
from .Line import Line

class Panel:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.coordinates(0.0, 0.0, 1.0, 1.0)
        self._root = tkinter.Tk()
        self._canvas = tkinter.Canvas(self._root, width=width, height=height)
        self._canvas.pack()
        self._fillcolor = "red"
        self._pencolor = "black"

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

    def color(self, value):
        self._fillcolor = value
        self._pencolor = value

    def fillcolor(self, value):
        self._fillcolor = value

    def pencolor(self, value):
        self._pencolor = value

    def circle(self, x, y, radius):
        return Circle(self, x, y, radius)

    def line(self, *args):
        if len(args) == 2:
            x1 = args[0][0]
            y1 = args[0][1]
            x2 = args[1][0]
            y2 = args[1][1]
        elif len(args) == 4:
            x1 = args[0]
            y1 = args[1]
            x2 = args[2]
            y2 = args[3]
        else:
            raise ValueError("Ungültige Anzahl Argumente")
        return Line(self, x1, y1, x2, y2)

    def start(self):
        self._root.mainloop()

    def _w(self, points):
        result = []
        for p in points:
            result.append(self._wx(p[0]))
            result.append(self._wy(p[1]))
        return result

    def _wx(self, x):
        return (x - self._minx) * self._scalex

    def _wy(self, y):
        return self._height - (self._miny - y) * self._scaley
