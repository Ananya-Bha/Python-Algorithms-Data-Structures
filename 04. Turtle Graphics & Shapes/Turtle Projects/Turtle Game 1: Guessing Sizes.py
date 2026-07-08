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
