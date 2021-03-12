from gpanel import *

coordinates(0, 0, 10, 10)


@event
def on_mouse_move(panel, x, y):
    print(panel, x, y)
