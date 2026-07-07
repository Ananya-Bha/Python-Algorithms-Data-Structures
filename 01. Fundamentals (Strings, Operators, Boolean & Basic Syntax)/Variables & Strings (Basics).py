import turtle as t
import random as r
t.shape("turtle")
s= t.Screen()
s.setup(height=400,width=500)
'''
Challenge 1
t.setpos(-200,0)
distance=r.randint(10,30)
for i in range(10):
  t.forward(distance)
  t.dot(5)
'''
'''
Challenge 2
for i in range(10):
  direction=r.randint(1,2)
  distance=r.randint(10,30)
  if direction==1:
    t.setheading(0)
    print("Facing East!")
    t.color("red")
  elif direction==2:
    t.setheading(180)
    print("Facing West!")
    t.color("green")
  t.forward(distance)
  t.dot(5)
'''
'''
Challenge 3
t.up()
t.setposition(0,200)
t.down()
for i in range(40):
  direction=r.randint(1,2)
  distance=r.randint(25,50)
  if direction==1:
      t.setheading(0)
      print("Facing East!")
      t.color("red")
  elif direction==2:
      t.setheading(180)
      print("Facing West!")
      t.color("green")
  t.forward(distance)
  t.dot(5)
  t.backward(distance)
  t.dot(5)
  t.forward(distance)
  t.up()
  t.setheading(270)
  t.forward(10)
  t.down()
'''

t.setheading(90)
def walk():
  for i in range(50):
    direction=r.randint(1,360)
    distance=r.randint(10,30)
    total=0
    t.forward(distance)
    t.dot(5)
    t.setheading(direction)
    total=total+distance
  t.up()
  t.setpos(0,0)
  t.down()
  turtle=0
  displacement=total/50
  int(displacement)
  turtle=+1
  print("Turtle",turtle,"has moved",displacement,"units.")
  

for i in range(3):
  color=r.randint(1,4)
  if color==1:
    t.color("red")
  elif color==2:
    t.color("blue")
  elif color==3:
    t.color("green")
  elif color==4:
    t.color("yellow")
  walk()
  

t.done()