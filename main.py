import random

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

# choose two random numbers between 1 and 10
a = random.randint(1, 10)
b = random.randint(1, 10)

# ask the user to add them together
user_answer_1 = input(f"What's {a} + {b}? ")

# congratulate them if they got it correct
if int(user_answer_1) == a + b:
    print()
    print("-------------------------------------------")
    emoji = random.choice(["⭐", "🏆", "✨"])
    print(f"{emoji} Wow, that's {bold}{y}amazing!{reset} You got it correct!")
    print("-------------------------------------------")
    print()

# now ask them to double the first number
user_answer_2 = input(f"What's {2} x {a}? ")

# congratulate them if they got it correct
if int(user_answer_2) == 2 * a:
    print()
    print("-------------------------------------------")
    emoji = random.choice(["⭐", "🏆", "✨"])
    print(f"{emoji} Wow, that's {bold}{y}amazing!{reset} You got it correct!")
    print("-------------------------------------------")
    print()

# now ask them to add 1 to the second number
user_answer_3 = input(f"What's 1 + {b}? ")

# congratulate them if they got it correct
if int(user_answer_3) == 1 + b:
    print()
    print("-------------------------------------------")
    emoji = random.choice(["⭐", "🏆", "✨"])
    print(f"{emoji} Wow, that's {bold}{y}amazing!{reset} You got it correct!")
    print("-------------------------------------------")
    print()

# ------------------------------------------------------
# CHALLENGE 2 - JUST ADD WATER
# ------------------------------------------------------




# -------------------------------------------------
# CHALLENGE 3 - IT ALL ADDS UP
# -------------------------------------------------



# -------------------------------------------------
# CHALLENGE 4 - MAKING A CALCULATOR
# -------------------------------------------------


# -------------------------------------------------
# CHALLENGE 5.1 - DEFAULT VALUES (LIVESTREAM)
# -------------------------------------------------





# -------------------------------------------------
# CHALLENGE 5.2 - DEFAULT VALUES (LIVESTREAM)
# -------------------------------------------------

def format_my_text(text, emoji="💡", colour=w, style=""):   
    output_text = f"{emoji} {colour}{style}{text}{reset}"
    return output_text


# -------------------------------------------------
# CHALLENGE 6 - DICE ROLLER 1
# -------------------------------------------------





# -------------------------------------------------
# CHALLENGE 7 - DICE ROLLER 2
# -------------------------------------------------




# -------------------------------------------------
# CHALLENGE 8 - DICE ROLLER 3
# -------------------------------------------------





# -------------------------------------------------
# CHALLENGE 9 - DICE ROLLER 4
# -------------------------------------------------




# -------------------------------------------------
# CHALLENGE 10 - DICE ROLLER 5
# -------------------------------------------------
