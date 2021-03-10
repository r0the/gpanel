from .Element import Element

class Line(Element):
    def __init__(self, panel, x1, y1, x2, y2):
        self._panel = panel
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._id = panel._canvas.create_line(
            self._coords,
            width=1,
            fill=panel._pencolor)
        panel._canvas.update()
        Element.__init__(self, panel)

    @property
    def _coords(self):
        return self._panel._w([(self._x1, self._y1), (self._x2, self._y2)])
