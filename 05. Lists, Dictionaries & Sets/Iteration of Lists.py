#challenge 1
'''
import random as r
my_numbers =[]
no=0
for i in range(10):
  num=r.randint(1,10)
  if num>5:
    my_numbers.append(num)
    no=no+1

print("There are",no,"numbers in the list")
print(my_numbers)
'''

#challenge 2 & 3
'''
import random as r
long_list =[]
for i in range(100):
  num=r.randint(1,3)
  if num == 3:
    print("Removing previous item...")
    if len(long_list)==0:
      print("No item to be removed!")
    else:
      long_list.pop() 
  long_list.append(num)
  print("Adding",num,"to the list")
  
print("\n Created a list with length:")
print(len(long_list))
'''
#Challenge 4 & 5
'''
import random as r
list = []
while True:
  item= input("Enter an Item, or q to quit:")
  if item == "q":
    if len(list) <2:
      print("You need at least 2 items in the list")
      continue
    break
  else:
    list.append(item)

print("You added",len(list),"items to the list")
print("A random item from you list:")
chosen_Item= r.choice(list)
print(chosen_Item)
'''



