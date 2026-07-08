#Scenario Based Question
cost_of_coach=550
cost_of_entry_ticket=30

students=0
while True:
    students=int(input("How many students are you taking on the trip?"))
    if students>45:
        print("Too many student! Cannot be allowed!")
    else:
        total_cost=cost_of_coach+(cost_of_entry_ticket*students)
        print(f"Your total cost is {total_cost}")
        break
'''
'''
#Length
print(len("Computer"))
#slicing
print("Computer Science"[0:4])
print("Computer Science"[2:])
print("Computer Science"[:4])
print("Computer Science"[:])
#upper
print("Computer Science".upper())
#lower
print("Computer Science".lower())


#Program 1:
user_ans=input("Enter a word:")
print(user_ans.upper())
#Program 2:
first_letter=user_ans[0].upper()
rest=user_ans[1:]
print(first_letter+rest)
#Program 3:
flipped=""
for i in user_ans:
    if i== i.upper():
        i=i.lower()
        flipped=flipped+i
    else:
        i=i.upper()
        flipped=flipped+i

print(flipped)
'''
#Activity 8.9
'''
num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)
num3=int(input("Enter a third number:"))
print(num3*(num1+num2))
print(num3* (num1-num2))
print((num1+num2)**num3)
'''

#Activity 8.10
'''
num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))

if num1==num2:
    print("These numbers are equal!")
else:
    print("These numbers are not equal")
    
if num1>num2:
    max=num1
    min=num2
    print(max," is greater than ",min)
    print("The smallest is ",min)
        
if num1<num2:
    max=num2
    min=num1
    print(max," is greater than ",min)
    print("The smallest is ",min)

num3=int(input("Enter a third number:"))

if num1==num2 and num1==num3:
    print("These numbers are equal!")
else:
    print("These numbers are not equal!")

numbers=[]
numbers.append(num1)
numbers.append(num2)
numbers.append(num3)


minimum= numbers[0]
for i in range(1,len(numbers)):
    compare=numbers[i]
    if compare< minimum:
        minimum=compare
print("Minimum number is:", minimum)

maximum= numbers[0]
for i in range(1,len(numbers)):
    compare=numbers[i]
    if compare> maximum:
        maximum=compare
print("Maximum number is:", maximum)
'''
#8.11 & 8.12
'''
for i in range(6):
    subject=input("Enter the first subject:")
    mark1=int(input("Enter marks of first test:"))
    mark2=int(input("Enter marks of second test:"))
    mark3=int(input("Enter marks of third test:"))
    mark4=int(input("Enter marks of fourth test:"))
    mark5=int(input("Enter marks of fifth test:"))

    marks=[]
    marks.append(mark1)
    marks.append(mark2)
    marks.append(mark3)
    marks.append(mark4)
    marks.append(mark5)
    
    average= (mark1+mark2+mark3+mark4+mark5)/5
    minimum= marks[0]
    for i in range(1,len(marks)):
        compare=marks[i]
        if compare< minimum:
            minimum=compare


    maximum= marks[0]
    for i in range(1,len(marks)):
        compare=marks[i]
        if compare> maximum:
            maximum=compare

    print("Minimum mark is:", minimum)
    print("Maximum mark is:", maximum)
    print("Average marks: ", average)
'''
#8.13
'''
sum=0
class_marks=[]
for i in range(20):
    mark=int(input("Enter student mark:"))
    class_marks.append(mark)
    sum=sum+mark

average=sum/20
maximum= class_marks[0]
for i in range(1,len(class_marks)):
    compare=class_marks[i]
    if compare> maximum:
        maximum=compare

minimum= class_marks[0]
for i in range(1,len(class_marks)):
    compare=class_marks[i]
    if compare< minimum:
        minimum=compare

print("Minimum mark is:", minimum)
print("Maximum mark is:", maximum)
print("Average marks: ", average)
