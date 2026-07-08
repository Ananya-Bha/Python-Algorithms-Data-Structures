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
