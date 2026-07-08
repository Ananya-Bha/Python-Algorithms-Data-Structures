
# -------------------------------------------------
# CREATIVE CONSOLE STYLES
# -------------------------------------------------

# FOREGROUND (text) colour escape codes
k = "\033[30m"  # black
r = "\033[31m"  # red
g = "\033[32m"  # green
y = "\033[33m"  # yellow
b = "\033[34m"  # blue
p = "\033[35m"  # purple
c = "\033[36m"  # cyan
w = "\033[37m"  # white
reset = "\033[0m"  # reset text back to normal

# BACKGROUND colour escape codes
kb = "\033[40m"  # black
rb = "\033[41m"  # red
gb = "\033[42m"  # green
yb = "\033[43m"  # yellow
bb = "\033[44m"  # blue
pb = "\033[45m"  # purple
cb = "\033[46m"  # cyan
wb = "\033[47m"  # white

# escape codes for styles
bold = "\033[1m"
faint = "\033[2m"
underline = "\033[4m"
invert = "\033[7m"

# ===========================================================
# 1️⃣ LESSON 9.5 FUNCTIONS I
# ===========================================================

# ------------------------------------------------------
# CHALLENGE 1 - MANY CONGRATULATIONS!
# ------------------------------------------------------
'''
def congratulate_user():
    print()
    print("-------------------------------------------")
    emoji = random.choice(["⭐", "🏆", "✨"])
    print(f"{emoji} Wow, that's {bold}{y}amazing!{reset} You got it correct!")
    print("-------------------------------------------")
    print()

# choose two random numbers between 1 and 10
a = random.randint(1, 10)
b = random.randint(1, 10)

# ask the user to add them together
user_answer_1 = input(f"What's {a} + {b}? ")

# congratulate them if they got it correct
if int(user_answer_1) == a + b:
    congratulate_user()

# now ask them to double the first number
user_answer_2 = input(f"What's {2} x {a}? ")

# congratulate them if they got it correct
if int(user_answer_2) == 2 * a:
    congratulate_user()

# now ask them to add 1 to the second number
user_answer_3 = input(f"What's 1 + {b}? ")

# congratulate them if they got it correct
if int(user_answer_3) == 1 + b:
    congratulate_user()
'''
# ------------------------------------------------------
# CHALLENGE 2 - JUST ADD WATER
# ------------------------------------------------------
'''
ingredients=[]
def just_add_water(ingredient): 
    print(ingredient,"and water")
    ingredients.append(ingredient)

ing = input("Enter an ingredient:")
just_add_water(ing)

for ingre in ingredients:
    just_add_water(ingre)
    '''
# -------------------------------------------------
# CHALLENGE 3 - IT ALL ADDS UP
# -------------------------------------------------
'''
#step 1
def add_numbers():
    a = int(input("a="))
    b= int(input("b="))
    print(str(a),"+",str(b),"=", a+b)

add_numbers()
#step 2
def Add_numbers():
    print(str(A),"+",str(B),"=",A+B)
    
A = int(input("A="))
B = int(input("B="))
Add_numbers()
'''
# -------------------------------------------------
# CHALLENGE 4 - MAKING A CALCULATOR
# -------------------------------------------------
'''
def calculator():
    if operation.lower()=="add":
        print()
        
    elif operation.lower()=="subtract":
        print(calculator(num_1 ,num_2, "subtract"))
    elif operation.lower(=="divide":
        print(calculator(num_1 ,num_2, "divide"))
    elif operation.lower()=="multiply":
        print(calculator(num_1 ,num_2, "multiply"))
    else:
        print("Invalid input")


num_1=int(input("Enter a number:"))
num_2=int(input("Enter another number:"))
operation=input("Enter the operation you would like to perform on these numbers")

calculator()
'''
# -------------------------------------------------
# CHALLENGE 5.1 - DEFAULT VALUES (LIVESTREAM)
# -------------------------------------------------
'''
def praise_rockethour(num_times=2,adjective="Fun!"):
    return ("Rockethour is "+adjective)*num_times
    
a=int(input("Enter a number:"))
b=input("Enter an adjective:")
print(praise_rockethour(a,b))
'''

# -------------------------------------------------
# CHALLENGE 5.2 - DEFAULT VALUES (LIVESTREAM)
# -------------------------------------------------
'''
def format_my_text(text, emoji="💡", colour=w, style=""):   
    output_text = f"{emoji} {colour}{style}{text}{reset}"
    return output_text

sentence=input("Enter a sentence:")
print(format_my_text(text=sentence, colour=b, style=bold, emoji="🪼"))
'''
# -------------------------------------------------
# CHALLENGE 6 - DICE ROLLER 1
# -------------------------------------------------
'''
import random as r

dice_rolls=[]
def store_dice_roll():
    num= r.randint(1,6)
    dice_rolls.append(num)
    

print("Rolling dice 2 times....")
for i in range(2):
    store_dice_roll()
print(dice_rolls)

print("Rolling dice 10 times....")
for i in range(8):
    store_dice_roll()
print(dice_rolls)
'''
# -------------------------------------------------
# CHALLENGE 7 - DICE ROLLER 2
# -------------------------------------------------
import random as r

dice_rolls=[]
def store_dice_roll(num_rolls):
    num= r.randint(1,6)
    dice_rolls.append(num)

num= int(input("How many times would you like to roll the dice?"))
print("Rolling the dice",num,"times")
for i in range(num):
    store_dice_roll(num_rolls=num)

print(list(dice_rolls))
