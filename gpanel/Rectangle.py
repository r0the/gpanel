from .Element import Element
from .Rect import Rect

class Rectangle(Element):
    def __init__(self, panel, x, y, width, height):
        self._panel = panel
        self._rect = Rect(x, y, width, height)
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._id = panel._canvas.create_rectangle(
            self._coords(),
            width=1,
            outline=panel._pencolor,
            fill=panel._fillcolor)
        panel.update()
        Element.__init__(self, panel)

    def _raw_coords(self):
        x = self._x
        y = self._y
        w = self._width
        h = self._height
        return [(x, y), (x + w, y + h)]
