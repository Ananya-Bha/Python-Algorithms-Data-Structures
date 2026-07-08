----------------------------
#Basic Arithmetic Calculator

num_1=int(input("Enter your first number:"))
num_2=int(input("Enter your second number:"))
operation=input("Enter the operation you would like to perform:")

if operation=="Division":
    print(num_1/num_2)
elif operation=="Addition":
    print(num_1+num_2)
elif operation=="Subtraction":
    print(num_1-num_2)
elif operation=="Multiplication":
    print(num_1*num_2)

-------------------------------
