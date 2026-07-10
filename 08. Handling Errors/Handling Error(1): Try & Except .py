shop = {"Blue": 2.99, "Green": 3.99, "Red": 0.99}
#Ask the user for a budget
#If they enter a non-integer, ask them to try again
try:
    budget = int(input("Enter you budget: "))
    print(budget)
except ValueError:
    print("Invalid Budget...\nPlease enter an integer value.")
    
#Function that calculates an average of a list
#Try and calculate the average
#Catch a ZeroDivisionError to display an appropriate message (display value)
#Return the calculated average
#Finally, return 0 

def average(numbers):
    try: 
        average = sum(numbers)/len(numbers)
        return average
    except ZeroDivisionError:
        print("Math Error, Division by Zero ...")
    finally:
        return 0

#Raise - Causes an exception to happen
#Program to input the age, age can't be negative

def getAge():
    age = input("Please enter age:")
    if age < 0:
        raise ValueError("Age can't be negative")
    return age
    
#Deposit function - two parameters: account, amount
#Error if amount is <0
#Return the new account amount
def deposit(account,amount):
    if amount <0:
        raise ValueError("Amount cannot be less than 0...")
    return account+amount


#Withdrawal function - two parameters: account, amount
#Error if amount is <0
#Error if ?
#Return the new account amount
def withdrawal(account,amount):
    if account <amount:
        raise ValueError("No money left to withdraw that amount")
    return account-amount
    if amount <0:
        raise ValueError("Amount cannot be less than 0...")
    return account+amount
    

#Exceptions that happen when reading/opening files:

try:
    with open("text.txt") as my_file:
        content = my_file.read()
except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("Insufficient permissions to open the file.")
except IOError:
    print("An I/O error occured that prevented opening the file.")
except OSError:
    print("Could not open the file.")

#Interactive calculator:
#Loop until user quits
#Allow user to choose 4 options (addition, subtraction, multiplication, division) (Exception)
#Allow user to input two values (Exception)
#Other exceptions (Division by zero)

def calculator():
    while True:
        print("Choose a caluclation method:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Divsion")
        try:
            choice = int(input("Enter method number (1/2/3/4) or 0 : "))
        except ValueError:
            print("Invalid Option... Please try again")
            continue
        if choice == 0:
            print("Switching Off..")
            break
        elif (choice >4) or (choice <0):
            print("Invalid Option.. Out of range")
            continue
        
        while True:
            try:
                num1= int(input("Enter your 1st number:"))
                num2= int(input("Enter your 2nd number:"))
                break
            except ValueError:
                print("Invalid numbers.. Please try again")
        if choice == 1:
            print(num1+num2)
        elif choice == 2:
            print(num1-num2)
        elif choice == 3:
            print(num1 * num2)
        elif choice == 4:
            try:
                print(num1/num2)
            except ZeroDivisionError:
                print("Math Error.... Division by Zero")
        
            
        



































    

        
    

