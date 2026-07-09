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
