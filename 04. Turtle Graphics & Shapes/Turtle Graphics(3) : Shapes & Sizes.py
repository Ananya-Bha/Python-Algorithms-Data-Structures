#challenge 1
'''
import turtle as t
t.shape("turtle")
t.setheading(90)
t.forward(100)
import time
time.sleep(100)
'''
#challenge 2
'''
import turtle as t
t.shape("turtle")
s = t.Screen()
s.setup(width=550, height=420)
t.setheading(360)
for i in range(10):
  t.forward(10)
  t.right(360)
'''
#challenge 3
'''
import turtle as t
t.shape("turtle")
s = t.Screen()
s.setup(width=550, height=420)
t.setheading(360)
for i in range(4):
  t.forward(50)
  t.left(90)
'''
#challenge 4
'''
import turtle as t
t.shape("turtle")
s = t.Screen()
s.setup(width=550, height=420)
t.setheading(360)
for i in range(360):
  t.forward(1)
  t.left(1)
'''
#challenge 5
'''
import turtle as t
t.shape("turtle")
s = t.Screen()
s.setup(width=550, height=420)
t.setheading(360)
for i in range(5):
  t.forward(50)
  t.left(72)
'''
#challenge 6
'''
import turtle as t
t.shape("turtle")
s = t.Screen()
s.setup(width=550, height=420)
t.setheading(360)
length=10
for i in range(36):
  t.forward(length+i)
  t.left(90)
'''
#challenge 7
'''
import turtle as t
t.shape("turtle")
s = t.Screen()
s.setup(width=550, height=420)
t.setheading(360)
spikes=int(input("How many spikes do you want?"))
for i in range(spikes):
  t.forward(50)
  t.backward(50)
  t.left(360/spikes)
'''
#challenge 8
'''
import turtle as t
t.shape("turtle")
s = t.Screen()
s.setup(width=550, height=420)
t.setheading(360)
length=5
for i in range(50):
  t.forward(length+i)
  t.left(30)
'''
#challenge 9
'''
import turtle as t
t.shape("turtle")
s = t.Screen()
s.setup(width=550, height=420)
t.setheading(360)
length=20
number=int(input("How many squares do you want?"))
for i in range(number):
  for i in range(4):
    t.forward(length)
    t.left(90)
  length=length+20
import time
time.sleep(100)
'''

#challenge 10
'''
import turtle as t
t.shape("turtle")
s = t.Screen()
s.setup(width=550, height=420)
t.setheading(360)
sides=int(input("Hoe many sides do you want?"))
for i in range(sides):
  t.forward(50)
  t.left(360/sides)
'''
#challenge 11
'''
import turtle as t
import random as r
t.shape("turtle")
s = t.Screen()
s.setup(width=550, height=420)
t.setheading(360)
for i in range(100):
  num=r.randint(1,360)
  t.left(num)
  t.forward(30)
'''
#Challenge 12
