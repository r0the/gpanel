class Element:
    def __init__(self, panel):
        self._panel = panel
        self._canvas = panel._canvas

    def _coords(self):
        return self._panel._p(self._raw_coords())

    def _update_coords(self):
        self._canvas.coords(self._id, self._coords())

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._update_coords()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self._update_coords()

    @property
    def fillcolor(self):
        return self._canvas.itemcget(self._id, "fill")

    @fillcolor.setter
    def fillcolor(self, value):
        self._canvas.itemconfig(self._id, fill=value)
