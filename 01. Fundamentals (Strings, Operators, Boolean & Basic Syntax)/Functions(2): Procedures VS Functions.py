#Notes
'''
Psuedocode Syntax for:
a)Procedure - doesnt do calculations, doesnt return a value 
PROCEDURE (Name of procedure)(Numer: INTEGERE)#Parameter
        OUTPUT"*********"
ENDPROCEDURE

CALL (Name of procedure)

b)Function - returns a value from calculations even if not told
def (Name of function):
    **Operations**

(Nam of function)()

-> Parameters: variable that store the values of the arguements passed to a procedure or function.Some but not all procedures and functions will have parameters.
'''

def check():
    while True:
        if answer=="yes":
            x=int(input("Enter a number"))
            stars(x)
        elif answer=="no":
            break

def stars(n):
    for i in range(n):
        print("*",end="")
    answer=input("\nContinue printing stars:").lower()
    check()
  
x=int(input("Enter a number"))
stars(x)
'''
#Function Questions & Answers
'''
Q1. Write a function called validPassword() that:
Takes a string as a parameter
Returns TRUE if the password length is at least 8 characters
Otherwise returns FALSE
Call this function in the main program to make it perform the required task.
'''
def validPassword(check):
    if len(check)>=8:
        print("True")
    else:
        print("False")

password=input("Enter your password:")
validPassword(password)
'''
Q2. Write a function called printNumbers() that:
Takes two integers start and end
Outputs all numbers from start to end (inclusive)
Outputs only numbers that are divisible by 3
Call this function in the main program to make it perform the required task.
'''
'''
def printNumbers(begin,stop):
    for i in range(begin,stop+1):
        print(i)

start=int(input("Where do you want to start:"))
end=int(input("Where do you want to end:"))
printNumbers(start,end)
