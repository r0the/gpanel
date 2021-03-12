from gpanel import *

def draw_corners():
    for x, y in corners:
        circle(x, y, 0.2)

def draw_lines():
    for p in corners:
        for q in corners:
            if p != q:
                line(p[0], p[1], q[0], q[1])

coordinates(0, 0, 10, 10)
corners = [(2, 3), (5, 2), (8, 5), (6, 8), (3, 7)]
draw_corners()
draw_lines()
