from .Element import Element

class Rectangle(Element):
    def __init__(self, panel, x1, y1, x2, y2):
        self._panel = panel
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._id = panel._canvas.create_rectangle(
            self._coords(),
            width=1,
            outline=panel._pencolor,
            fill=panel._fillcolor)
        panel.update()
        Element.__init__(self, panel)

    def _raw_coords(self):
        return [(self._x1, self._y1), (self._x2, self._y2)]
