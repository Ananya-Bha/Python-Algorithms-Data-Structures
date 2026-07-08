#challenge 1
'''
my_number = int(input("Enter you number here:"))
my_number = my_number +1
print("Your new number is:",my_number)
'''
#challenge 2
'''
my_number=int(input("Enter your first number here:"))
add=int(input("Enter your second number here:"))
my_number=my_number+add
print("Your new number is:",my_number)
'''
#challenge 3
'''
my_number=0
print("Starting from 0...")
while True:
  print("Your number is:",my_number)
  add = input("Enter a number to add ,or q to quit:")
  if add == "q":
    break
  else:
    my_number = my_number + int(add)
print("Your number is:",my_number)    
'''
#challenge 4
'''
my_number = int(input("Enter your number:"))
while True:
  print("Your number is:",my_number)
  print("1. Add one to your number\n2. Add a custom number number\n3.Halve your number\n4. Subtract 1 from your number\nq. Quit")
  choice = input("Enter your choice:")
  if choice == "1":
    my_number = my_number + 1
  elif choice== "2":
    add=input("Enter your number to add:")
    my_number = my_number +int(add)
  elif choice=="3":
    my_number=my_number/2
  elif choice=="4":
    my_number=my_number-1
  else:
    break
print("Your number is:",my_number)    
'''
#challenge 5
x = 0
y = 0
while True:
  print("Your current poistion is:","(",x,",",y,")")
  num_x = int(input("Enter your x coordinate:"))
  num_y = int(input("Enter your y coordinate:"))
  if num_x==0 and num_y==0:
    break
  else:
    x = x + num_x
    y = y + num_y
print("NO MOVEMENT DETECTED\nExiting.....\nFinal position is:","(",x,",",y,")")
  
