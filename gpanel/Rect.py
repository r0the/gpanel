class Rect:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __repr__(self):
        return "<%s (x: %s, y: %s, width: %s, height: %s)>" % (
            self.__class__.__name__, self._x, self._y, self._width, self._height)

    def _get_width(self):
        return self._width

    def _set_width(self, width):
        self._width = width

    width = property(_get_width, _set_width)
    
    def _get_height(self):
        return self._height

    def _set_height(self, height):
        self._height = height

    height = property(_get_height, _set_height)
    
    def _get_left(self):
        return self._x

    def _set_left(self, left):
        self._x = left

    left = property(_get_left, _set_left)

    def _get_right(self):
        return self._x + self._width

    def _set_right(self, right):
        self._x = right - self._width

    right = property(_get_right, _set_right)

    def _get_top(self):
        return self._y + self._height

    def _set_top(self, top):
        self._y = top - self._height

    top = property(_get_top, _set_top)

    def _get_bottom(self):
        return self._y

    def _set_bottom(self, bottom):
        self._y = bottom

    bottom = property(_get_bottom, _set_bottom)

    def _get_x(self):
        return self._x + self._width / 2

    def _set_x(self, x):
        self._x = x - self._width / 2

    x = property(_get_x, _set_x)

    def _get_y(self):
        return self._y + self._height / 2

    def _set_y(self, x):
        self._y = y - self._height / 2

    y = property(_get_y, _set_y)
