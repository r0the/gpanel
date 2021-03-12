from .Element import Element

class Circle(Element):
    def __init__(self, panel, x, y, radius):
        Element.__init__(self, panel)
        self._panel = panel
        self._x = x
        self._y = y
        self._radius = radius
        self._id = panel._canvas.create_oval(
            self._coords(),
            fill=panel._fillcolor,
            outline=panel._pencolor)
        panel.update()

    def _raw_coords(self):
        r = self._radius
        x = self._x
        y = self._y
        return [(x - r, y - r), (x + r, y + r)]

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._update_coords()
