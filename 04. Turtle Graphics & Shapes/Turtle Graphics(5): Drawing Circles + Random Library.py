import turtle as t
import random as r
s= t.Screen()
s.setup(height=300,width=300)
t.shape("turtle")
t.speed("slow")
t.pensize(10)

#choose random values
num1=r.randint(1,100)
num2=r.randint(1,(100-num1))
num3=r.randint(1,(100-num1-num2))
num4=r.randint(1,(100-num1-num2-num3))
num5=r.randint(1,(100-num1-num2-num3-num4))
#draw circle
t.setheading(0)
#Draw part 1
print("Drawing",num1,"....")
for i in range(num1):
  t.color("red")
  t.right(360/100)
  t.forward(2)

#Draw part 2
print("Drawing",num2,"....")
for i in range(num2):
  t.color("green")
  t.right(360/100)
  t.forward(2)


#Draw part 3
print("Drawing",num3,"....")
for i in range(num3):
  t.color("yellow")
  t.right(360/100)
  t.forward(2)

#Draw part 4
print("Drawing",num4,"....")
for i in range(num4):
  t.color("blue")
  t.right(360/100)
  t.forward(2)

#Draw part 5
print("Drawing",num5,"....")
for i in range(num5):
  t.color("pink")
  t.right(360/100)
  t.forward(2)



t.done()
