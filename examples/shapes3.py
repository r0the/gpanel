from gpanel import *

title("Schachbrett")
coordinates(0, 0, 8, 8)

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            rectangle(i, j, 1, 1)
