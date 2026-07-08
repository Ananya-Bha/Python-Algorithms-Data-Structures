#challenge 1
'''
while(True):
  name = str(input("Enter the name of this programming language:"))
  name=name.lower()
  if name=="python":
    print("Correct!")
    break
  else:
    print("Incorrect!")
print("I'm glad we could agree on this!")
'''
#challenge 2
'''
answer = str(input("What is the best snack?"))
answer=answer.lower()
if answer == "mango" or answer == "strawberry":
  print("Yes, that is the best snack!")
else:
  print("I am not to sure about that...")
'''
#challenge 3
'''
while True:
  number = int(input("What is 154711 - 61711 :"))
  if number > (154711-61711) :
    print("That's to high!")
  elif number< (154711-61711):
    print("That's too low!")
  else:
    print("Yayy! You got it!")
    break
    
  print("Ok") 
 '''
#Challenge 4
'''
number = int(input("Enter a number here:"))
if number < 10 :
  print("That's a small number!")
elif number <100 and number >90:
  print("That number is very close to 100!")
elif number%2==0:
  print("That's a large even number!")
else:
  print("I don't know about that!")
'''

#challenge 5
while True:
  sum1=100
  num2=700
  
  number = int(input("I am thinking of a number between", sum1 ,"&",num2,"\n What is it?"))
  if number == 560 :
    print("Correct!Good Job!")
    break
  elif number >560:
    print("That's too high!")
    num2 = number
    
  else:
    print("That's too low!")
    num1 = number


  
