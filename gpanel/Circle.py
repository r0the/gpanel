from .Element import Element

class Circle(Element):
    def __init__(self, panel, x, y, radius):
        self._panel = panel
        self._radius = radius
        self._x = x
        self._y = y
        self._id = panel._canvas.create_oval(
            self._coords,
            fill=panel._fillcolor,
            outline=panel._pencolor)
        panel._canvas.update()
        Element.__init__(self, panel)

    @property
    def _coords(self):
        r = self._radius
        x = self._x
        y = self._y
        return self._panel._w([(x - r, y - r), (x + r, y + r)])

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._update_coords()
