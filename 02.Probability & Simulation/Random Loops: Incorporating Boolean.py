# challenge 2
"""
import random as r
number=r.random()
print("Step 1\n",number)
number *=10
print("Step2\n",number)
number +=1
print("Step3\n",number)
number = int(number)
print("Step4\n",number)
"""

# challenge 3
"""
import random as r
number=r.randint(1,10)
print("Step 1\n",number,"\nThat's all!")
"""

# challenge 4
"""
import random as r
year=r.randint(2010,2024)
print("I was born in 2010")
print("It is 2024 right now")
print("In",year,"I was",year-2010,"years old")
"""
# challenge 5


print("Welcome to the Python Archery Range")
while True:
    import random as r

    attempt = r.randint(1, 10)
    print(attempt)
    if attempt < 5 and attempt >= 1:
        print("Too low!")
        print("You missed by -", 5 - attempt, "points")
        option = input("Try again?\n")
        if option == "":
            continue
        else:
            break
    elif attempt > 5 and attempt <= 10:
        print("Too high!")
        print("You missed by +", attempt - 5, "points")
        option = input("Try again?\n")
        if option == "":
            continue
        else:
            break
    else:
        print("Bullseye!")
        break

# challenge 6
print("Welcome to the Python Archery Range")
averagemiss = 0
miss = 0
for i in range(1, 100):
    import random as r

    attempt = r.randint(1, 10)
    print(attempt)
    if attempt < 5 and attempt >= 1:
        miss = 5 - attempt
        print("You missed by -", miss, "points")
        averagemiss = averagemiss + miss
    elif attempt > 5 and attempt <= 10:
        miss = attempt - 5
        print("You missed by +", miss, "points")
        averagemiss = averagemiss + miss
    else:
        print("Bullseye!")
averagemiss = averagemiss / 100
print("Your average miss was:", averagemiss)
