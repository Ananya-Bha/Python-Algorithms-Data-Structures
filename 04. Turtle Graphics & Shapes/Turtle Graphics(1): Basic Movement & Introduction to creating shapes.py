#Challenge 1
'''
import turtle as t
t.forward(50)
t.shape("turtle")
'''
#Challenge 2
'''
import turtle as t
t.shape("turtle")
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
'''
#challenge 3
'''
import turtle as t
t.shape("turtle")
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
'''
#Challenge 4
'''
import turtle as t
t.shape("turtle")
t.forward(50)
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)
'''
#Challenge 5
'''
import turtle as t
t.shape("turtle")
t.setheading(180)
t.right(130)
t.forward(50)
t.left(130)
t.forward(50)
t.right(130)
t.forward(50)
t.left(130)
t.forward(50)
'''
#Challenge 6
'''
import turtle as t
t.shape("turtle")
t.setheading(90)
t.forward(50)
t.backward(50)
t.right(30)
t.forward(50)
t.backward(50)
t.right(30)
t.forward(50)
t.backward(50)
t.right(30)
t.forward(50)
t.backward(50)
'''
#Challenge 7
'''
import turtle as t
t.shape("turtle")
length=int(input("Enter a side length:"))
t.forward(length)
t.right(90)
t.forward(length)
t.right(90)
t.forward(length)
t.right(90)
t.forward(length)
'''
#Challenge 8
'''
import turtle as t
t.shape("turtle")
t.setheading(90)
t.forward(50)
t.right(90)
t.forward(50)
t.backward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
'''
#Challenge 9
'''
import turtle as t
t.shape("turtle")
t.setheading(90)
t.up()
t.forward(50)
t.down()
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.backward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
'''
#Challenge 10
'''
import turtle as t
t.shape("turtle")
num=int(input("Enter a number:"))
for i in range(0,num):
  t.forward(50)
  t.right(180)
  t.forward(50)
  t.right(180)
'''
#Challenge 11
'''
import turtle as t
t.shape("turtle")
import random as r
num=r.randint(1,179)
print("A triangle with an angle of",num,"degrees")
t.forward(50)
t.right(num)
t.right(180-((180-num)/2))
t.forward(50)
t.setpos(0,0)
'''
#Challenge 12
'''
import turtle as t
t.shape("turtle")
for i in range(5):
  t.right(180-36)
  t.forward(50)
'''
#Challenge 13
'''
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
'''
#Challenge 14
'''
import turtle as t
t.shape("turtle")
t.setheading(90)
t.forward(50)
p1=t.position()
t.backward(50)
t.right(30)
t.forward(50)
p2=t.position()
t.backward(50)
t.right(30)
t.forward(50)
p3=t.position()
t.backward(50)
t.right(30)
t.forward(50)
t.pencolor("red")
t.setpos(p3)
t.setpos(p2)
t.setpos(p1)
t.setpos(0,0)
'''
#Challenge 15

'''
import turtle as t
t.shape("turtle")
t.setheading(270)
t.forward(70)
t.penup()
t.forward(30)
t.pendown()
t.forward(70)
p2=t.position()
t.right(180)
t.forward(70)
t.penup()
t.forward(30)
t.pendown()
t.forward(70)
t.right(90)
t.penup()
t.forward(20)
t.pendown()
t.right(90)
t.forward(70)
t.penup()
t.forward(30)
t.pendown()
t.forward(70)
p4=t.position()
t.right(180)
t.forward(70)
t.penup()
t.forward(30)
t.pendown()
t.forward(70)
t.right(90)
t.penup()
t.forward(20)
t.pendown()
t.right(90)
t.forward(70)
t.penup()
t.forward(30)
t.pendown()
t.forward(70)
t.right(45)
t.forward(30)
'''
'''
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
'''



'''
import turtle as t
t.shape("turtle")
import random as r
num=r.randint(1,179)
print("A triangle with an angle of",num,"degrees")
t.forward(50)
t.right(num)
t.right(180-((180-num)/2))
t.forward(50)
t.setpos(0,0)
'''

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
