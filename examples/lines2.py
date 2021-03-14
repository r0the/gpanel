from gpanel import *
from time import sleep

coordinates(0, 0, 10, 10)

for i in range(11):
   for k in range (11):
      line(i, 0, k, 10)
      sleep(0.1)
    
for i in range(11):
   for k in range (11):
      line(0, i, 10, k)
      sleep(0.1)
