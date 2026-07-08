#challenge 1
'''
import turtle as t
t.shape("turtle")
t.color("red","blue")
t.begin_fill()
for i in range(4):
  t.forward(50)
  t.left(90)
t.end_fill()

t.done()
'''
#challenge 2
'''
import turtle as t
t.shape("turtle")
for i in range(15):
  t.forward(5)
  t.pensize(i)


t.done()
'''

#challenge 3
'''
import turtle as t
t.shape("turtle")
t.color("green","yellow")
t.pensize(3)
t.begin_fill()
for i in range(5):
  t.forward(50)
  t.left(180-108)
t.end_fill()
t.done()
'''
#challenge 4
'''
import turtle as t
t.shape("turtle")
t.color("green")
for i in range(180):
  t.forward(1)
  t.left(1)
  t.pensize(i/10)
t.color("blue")
for i in range(180):
  t.forward(1)
  t.left(1)
  t.pensize(i/10)
t.done()
'''
#challenge 5
'''
import turtle as t
t.shape("turtle")
import random as r
r= r.randint(1,4)
if r == 1:
  t.color("red","red")
  t.begin_fill()
  for i in range(2):
    t.forward(50)
    t.left(70)
    t.forward(50)
    t.left(110)
  t.end_fill()
elif r == 2:
  t.color("blue","blue")
  t.begin_fill()
  for i in range(2):
    t.forward(50)
    t.left(70)
    t.forward(50)
    t.left(110)
  t.end_fill()
elif r == 3:
  t.color("green","green")
  t.begin_fill()
  for i in range(2):
    t.forward(50)
    t.left(70)
    t.forward(50)
    t.left(110)
  t.end_fill()
else:
  t.color("yellow","yellow")
  t.begin_fill()
  for i in range(2):
    t.forward(50)
    t.left(70)
    t.forward(50)
    t.left(110)
  t.end_fill()
t.done()
'''
#challenge 6
'''
import turtle as t
t.shape("turtle")

t.begin_fill()
for i in range(2):
  for i in range(180):
    t.color("pink")
    t.forward(1)
    t.left(1)
  t.end_fill() 
  t.begin_fill()
  for i in range(180):
    t.color("orange")
    t.forward(1)
    t.right(1)
  t.end_fill()
t.done()
'''
import turtle as t
t.shape("turtle")

t.begin_fill()
for i in range(2):
  for i in range(180):
    t.color("pink")
    t.forward(1)
    t.left(1)
  t.end_fill() 
  t.begin_fill()
  for i in range(180):
    t.color("orange")
    t.forward(1)
    t.right(1)
  t.end_fill()
t.done()
  
