class Rect:
    def __init__(self, left, bottom, width, height):
        self._left = left
        self._bottom = bottom
        self._width = width
        self._height = height

    def __copy__(self):
        return Rect(self._left, self._bottom, self._width, self._height)

    def __repr__(self):
        return "<%s (left: %s, bottom: %s, width: %s, height: %s)>" % (
            self.__class__.__name__, self._left, self._bottom, self._width, self._height)

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
        return self._left

    def _set_left(self, left):
        self._left = left

    left = property(_get_left, _set_left)

    def _get_right(self):
        return self._left + self._width

    def _set_right(self, right):
        self._left = right - self._width

    right = property(_get_right, _set_right)

    def _get_bottom(self):
        return self._bottom

    def _set_bottom(self, bottom):
        self._bottom = bottom

    bottom = property(_get_bottom, _set_bottom)

    def _get_top(self):
        return self._bottom + self._height

    def _set_top(self, top):
        self._bottom = top - self._height

    top = property(_get_top, _set_top)

    def _get_x(self):
        return self._left + self._width / 2

    def _set_x(self, x):
        self._left = x - self._width / 2

    x = property(_get_x, _set_x)

    def _get_y(self):
        return self._bottom + self._height / 2

    def _set_y(self, x):
        self._bottom = y - self._height / 2

    y = property(_get_y, _set_y)
