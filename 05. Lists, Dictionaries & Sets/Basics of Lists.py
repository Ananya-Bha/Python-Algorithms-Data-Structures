#Challenge 1
'''
list_1 =["🍎Apple","🍌Banana","🍓Strawberry",]
list_2=[]
list_2.append("🍎Apple")
list_2.append("🍌Banana")
list_2.append("🍓Strawberry")
print(list_1)
print(list_2)
if list_1==list_2:
  print("\nThe lists are the same")
else:
  print("They are different!")
'''

#Challenge 2
'''
import random as r
dice_roll =[]
for i in range(5):
  dice_roll.append(r.randint(1,6))

print("\n🎲",dice_roll)
'''

#Challenge 3 & 4
'''
i=0
my_list =[]
for i in range(5):
  my_list.append(input(f"Enter word {i +1} :"))

print("\nYou enetered 5 words!")
  
for word in my_list:
  print("\nI Like",word)
'''

#Challenge 5

my_list =[]
for i in range(5):
  word=input(f"Enter word {i +1} :")
  my_list.append(len(word))

print("\nYou enetered 5 words!")

print("The lengths of the words you inputed are:")
print(my_list)
