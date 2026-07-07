'''
#challenge 1,2,3,4
import turtle as t
import random as r
s=t.Screen()
s.setup(height=400,width=500)
t.shape("turtle")
t.color("green")
for i in range(2):
  t.forward(100)
  t.dot(5)
t.home()
t.color("black")
t.pensize(4)
distance=r.randint(1,20)*10
t.forward(distance)
for i in range(3):
  geuss=int(input("how far did the turtle move?"))
  if geuss==distance:
    print("correct!")
    break
  elif geuss>distance:
    print("too high")
  else:
    print("too low")
print("You have run out of chances to geuss!")
t.done()
'''
#challenge 5
'''
import turtle as t
import random as r
s=t.Screen()
s.setup(height=400,width=500)
t.shape("turtle")
t.color("blue")
for i in range(4):
  t.setpos(0,0)
  t.left(90)
  for i in range(3):
    t.forward(100)
    t.dot(5)
t.home()
size=r.randint(1,15)*10
tries=0
t.color("black")
t.dot(size)
for i in range(3):
  geuss=int(input("how big was the dot?"))
  if geuss==size:
    print("correct!")
    tries=tries+1
    print("You took",tries,"tries to guess the size of the dot.")
    break
  elif geuss>size:
    print("too big")
    tries=tries+1
    t.color("red")
    t.dot(geuss)
    t.color("black")
    t.dot(size)
  else:
    print("too small")
    tries=tries+1
    t.color("green")
    t.dot(geuss)
print("You took",tries,"tries to guess the size of the dot.")
t.done()
'''
#challenge 8
'''
import turtle as t
import random as r
s=t.Screen()
s.setup(height=400,width=500)
t.color("blue")
t.shape("turtle")
for i in range(12):
  t.forward(50)
  t.dot(5)
  t.backward(50)
  t.left(30)
t.home()
print("You have 10 chances to guess the angle the turtle is facing.")
angle=r.randint(1,360)
t.home()
t.left(angle)
t.color("green")
t.forward(50)
for i in range(5):
  geuss=int(input("what angle is the turtle facing?"))
  if geuss==angle:
    print("Correct!")
    t.home()
    t.pensize(4)
    t.color("green")
    t.left(angle)
    t.forward(50)
    t.dot(6)
    break
  elif geuss>angle:
    print("Too high")
    t.home()
    t.color("red")
    t.left(geuss)
    t.forward(50)
    t.home()
  elif geuss<angle:
    print("Too low")
    t.home()
    t.color("red")
    t.left(geuss)
    t.forward(50)
    t.home()
  elif geuss>360:
    print("That is not a valid angle")

t.done()
'''
'''
import turtle as t
import random as r
s=t.Screen()
s.setup(height=400,width=500)
t.shape("turtle")
t.color("green")
for i in range(2):
  t.forward(100)
  t.dot(5)
t.home()
t.color("black")
t.pensize(4)
distance=r.randint(1,20)*10
t.forward(distance)
for i in range(3):
  geuss=int(input("how far did the turtle move?"))
  if geuss==distance:
    print("correct!")
    break
  elif geuss>distance:
    print("too high")
  else:
    print("too low")
print("You have run out of chances to guess!")
t.done()
'''
import turtle as t
import random as r
s=t.Screen()
s.setup(height=400,width=500)
t.color("blue")
t.shape("turtle")
for i in range(12):
  t.forward(50)
  t.dot(5)
  t.backward(50)
  t.left(30)
t.home()
print("You have 10 chances to guess the angle the turtle is facing.")
angle=r.randint(1,360)
t.home()
t.left(angle)
t.color("green")
t.forward(50)
for i in range(5):
  geuss=int(input("what angle is the turtle facing?"))
  if geuss==angle:
    print("Correct!")
    t.home()
    t.pensize(4)
    t.color("green")
    t.left(angle)
    t.forward(50)
    t.dot(6)
    break
  elif geuss>angle:
    print("Too high")
    t.home()
    t.color("red")
    t.left(geuss)
    t.forward(50)
    t.home()
  elif geuss<angle:
    print("Too low")
    t.home()
    t.color("red")
    t.left(geuss)
    t.forward(50)
    t.home()
  elif geuss>360:
    print("That is not a valid angle")

t.done()
