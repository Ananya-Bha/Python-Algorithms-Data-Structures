#challenge 1
'''
for i in range(0,10):
  print("Hello number",i)
'''
#challenge 2
'''
for i in range(0,10):
  print("Practice makes perfect!")
'''
#challenge 3
'''
number = int(input("How many banaanas do you want?"))
for i in range(0,number):
  print("Banana")
'''
#challenge 4
'''
print("Counting to 20...")
for i in range(0,21):
  print(i)
'''
#challenge 5
'''
import random as r
print("Thinking of 15 numbers...")
for i in range(0,15):
  number = r.randint(1,10)
  print(number)
'''
#challenge 6
'''
import random as r
integer=r.randint(1,10)
print("Let's roll a dice",integer, "times")
for i in range(0,integer):
  number=r.randint(1,6)
  print("Dice roll",i+1,"out of",integer)
  print("......You rolled a",number,"!\n")
'''
#challenge 7
'''
number=int(input("Till how many numbers should l check?"))
for i in range(0,number):
  if i%3==0:
    print(i)
'''
#challenge 8
'''
total=0
number=int(input("Till how many numbers should l check?"))
for i in range(0,number):
  if i%3==0:
    total=total+1
    print(i)
print("I have found",total,"numbers divisible by 3")
'''
#challenge 9
'''
number=int(input("Enter a starting number:"))
for i in range(number,number+10):
  print(i)
'''
#challenge 10
'''
print("STARTING COUNTDOWN")
num=10
for i in range(0,10):
  num=10-i
  print("T MINUS",num)
print("BLAST OFF")
'''
#challenge 11
'''
import random as r
for i in range(0,12):
  number=r.randint(i,i+1)
  print("Number between",i,"and",i+1)
  print(".......",number)
'''
#challenge 12
'''
import random as r
dot="."
cross="X"
for i in range(0,10):
  number=r.randint(1,10)
  print(dot*(number-1),cross,dot*(10-number))
'''
#challenge 13
'''
print("Making a Square...")
for i in range(0,10):
  print(str(0)*10)
'''
#challenge 14

rows = int(input("Rows: "))
columns = int(input("Columns: "))

for i in range(0, rows):
    if i == 0 or i == rows - 1:
        print("X" * columns)  
    else:
        print("X" + "." * (columns - 2) + "X")
