import turtle as t
t.shape("turtle")
sides= int(input("How many sides do you want?"))
if sides>2:
  length=300/sides
  angle=360/sides
  for i in range(sides):
    t.forward(length)
    t.right(angle)
else:
  print("Please enter a number greater than 2")

import time
time.sleep(100)
