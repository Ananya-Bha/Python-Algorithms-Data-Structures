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
# 1️⃣ LESSON 9.7 STRONGER STRINGS
# ===========================================================

# -------------------------------------------------
# CHALLENGE 1 - INDEXES IN LISTS
# -------------------------------------------------

words = [
    "awesome", "bananas", "I", "gravy", "flying", "am", "penguins", "love"
]
indexes = [0, 1, 2, 3, 4, 5, 6, 7]

# 🧑‍💻 YOUR CODE HERE

print(words[0])
for i in indexes:
    print(words[i])

print(f"{words[2]} {words[5]} {words[3]}")

# -------------------------------------------------
# CHALLENGE 2 - INDEXES IN STRINGS
# -------------------------------------------------
#       0123456789
code = "YUEISNTHTESMRTBHZEMWAQTJURITXSA IOUZA"

# 🧑‍💻 YOUR CODE HERE
'''
print(code[2])
print(code[5])
print(code[6])
'''

# -------------------------------------------------
# CHALLENGE 3 - DECIPHERING THE CODE
# -------------------------------------------------

codex = [2, 5, 8, 9, 12, 31, 13, 15, 17, 31, 18, 20, 22, 25, 26, 28]

for i in codex:
    print(code[i])
# 🧑‍💻 YOUR CODE HERE



# -------------------------------------------------
# CHALLENGE 4 - DECIPHERING THE CODE
# -------------------------------------------------

# 🧑‍💻 YOUR CODE HERE
print(f"{code[2]}{code[5]}{code[8]}{code[9]}{code[12]}{code[31]}{code[13]}{code[15]}{code[17]}{code[31]} {code[18]}{code[20]}{code[22]}{code[25]}{code[26]}{code[28]}")

# -------------------------------------------------
# CHALLENGE 5 - MAKE IT A FUNCTION
# -------------------------------------------------
     #   0123456789
code2 = "LTQASFKXGDOEPTHWLEPNREIDNPQINLLN TDKFJDIUZK"
codex2 = [1, 3, 6, 11, 32, 13, 14, 17, 32, 20, 21, 23, 32, 25, 27, 29, 30]



# 🧑‍💻 YOUR CODE HERE
'''
def decoder(text, coder):
    message =""
    for i in coder:
        message +=text[i]
    print(message)

decoder(code2, codex2)
'''
