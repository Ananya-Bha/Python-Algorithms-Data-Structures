import random
import turtle

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
# 1️⃣ LESSON 9.3 DICTIONARIES I
# ===========================================================

# -------------------------------------------------
# CHALLENGE 1 - DICTIONARY CREATION AND LOOKUPS
# -------------------------------------------------

# create a dictionary with two entries using the text below
"""
1. polygon
A flat shape with straight sides. Think of it like a drawing made by connecting dots with straight lines.

2. vertex (vertices)
The corners or points where the sides of a polygon meet. If you draw a shape, the sharp corners where the lines end are the vertices.
"""
# [🧑‍💻 YOUR DICTIONARY CODE HERE]

# 🚀 BONUS! Make the most important part of each definition bold.
# You'll find escape codes at the top of the file.

# check the data type of your dictionary and print it
# [🧑‍💻 YOUR CODE HERE]

# print the whole dictionary, just to see what it looks like
# [🧑‍💻 YOUR CODE HERE]

# lookup a single entry from the dictionary using .get()
# [🧑‍💻 YOUR CODE HERE]

# -------------------------------------------------
# CHALLENGE 2 - UPDATING THE DICTIONARY
# -------------------------------------------------

# add one new entry to the dictionary using square brackets
"""
3. side
The straight edges that make up the polygon. If you think of your polygon as a fence, the sides are the pieces of wood between each post (vertex).
"""
# [🧑‍💻 YOUR CODE HERE]


# create a NEW dictionary for the names of six polygons
# 🎨 put the number of sides in BOLD and in DIFFERENT COLOURS
"""
1. triangle: A polygon with three sides.
2. quadrilateral: A polygon with four sides.
3. pentagon: A polygon with five sides.
4. hexagon: A polygon with six sides.
5. heptagon: A polygon with seven sides.
6. octagon: A polygon with eight sides.
"""
# [🧑‍💻 YOUR CODE HERE]

# update your original dictionary with this new dictionary
# [🧑‍💻 YOUR CODE HERE]

# -------------------------------------------------
# CHALLENGE 3 - DICTIONARY FORMATTING
# -------------------------------------------------


# keep asking the user for a word to look up until they quit
# then output that word and its meaning to the console
# 🚀 BONUS! Format the output nicely with text styles, white space etc.

# uncomment the code below before you start
# while True:
#     word = input("Which word should I look up? (q to quit) ")
#     if word == "q":
#         break
#     else:
#         output = "[🧑‍💻 YOUR CODE HERE]"
#         print(output)


# ===========================================================
# 2️⃣ LESSON 9.4 DICTIONARIES II
# ===========================================================

# -------------------------------------------------
# CHALLENGE 4 - KEYS AND VALUES FROM DICTIONARIES
# -------------------------------------------------

# get a LIST of polygon names from the dictionary without retyping them
# [🧑‍💻 YOUR CODE HERE]

# iterate through the list and print each polygon on a separate line
# uncomment the code below before you start
# print("\nPOLYGONS")
# # [🧑‍💻 YOUR CODE HERE]

# # get a LIST of definitions of each polygon from the dictionary
# # [🧑‍💻 YOUR CODE HERE]

# # iterate through the list and print each definition on a separate line
# print("\nDEFINITIONS")
# [🧑‍💻 YOUR CODE HERE]


# -------------------------------------------------
# CHALLENGE 5 - ZIP! DICTIONARIES FROM LISTS
# -------------------------------------------------

# here is a list of sides for polygons from triangles to octagons
sides_list = [3, 4, 5, 6, 7, 8]

# create dictionary with sides as keys and polygon names as values
# [🧑‍💻 YOUR CODE HERE]

# print it to see that it's a dictionary
# uncomment the line below before you start
# print("\nDICTIONARY")
# [🧑‍💻 YOUR CODE HERE]

# choose a random number of sides from the list
num = random.choice(sides_list)

# lookup and print the matching POLYGON NAME
# [🧑‍💻 YOUR CODE HERE]

# lookup and print the matching DEFINITION for that polygon
# [🧑‍💻 YOUR CODE HERE]

# -------------------------------------------------
# CHALLENGE 6 - EXTERNAL ANGLES OF POLYGONS
# -------------------------------------------------

# create an empty dictionary
# [🧑‍💻 YOUR CODE HERE]

# calculate the internal angles for each number of sides
for num_sides in sides_list:
    # calculate the size of the external angle
    angle = round(360 / num_sides, 1)
    # add the number of sides and angle to the dictionary
    # [🧑‍💻 YOUR CODE HERE]

# print the dictionary, just to check your output
# [🧑‍💻 YOUR CODE HERE]

# -------------------------------------------------
# CHALLENGE 7 - DICTIONARIES WITH THE SAME KEYS
# -------------------------------------------------

# make multiple dictionaries using the same keys

# this is a list of VARIABLES, containing ANSI escape codes from the top of the script
console_colours = [r, g, y, b, p, c]

# lits of some appropriate emoji (you can customise these later)
reaction_emojis = ["❤️", "💚", "💛", "💙", "💜", "🩵"]
number_emojis = ["3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"]

# now use zip to make dictionaries using the above lists
# [🧑‍💻 YOUR CODE HERE]

# print each dictionary, just to check your output
# [🧑‍💻 YOUR CODE HERE]

# -------------------------------------------------
# CHALLENGE 8 - CONSOLE OUTPUT
# -------------------------------------------------

# ask the user how many sides the shape must have and store it in a variable
# uncomment the line below before you start 
# num_sides = int(input("❓ How many sides, from 3 to 8? "))

# lookup all the "ingredients" you need before printing
# [🧑‍💻 YOUR CODE HERE]

# print to the console to match the example
# 💡HINT: Use f-strings. Here is the degree symbol: °
# [🧑‍💻 YOUR CODE HERE]


# -------------------------------------------------
# CHALLENGE 9 - DRAWING POLYGONS IN TURTLE
# -------------------------------------------------

# uncomment the line below before you start
# input("\n🐢 Let's ask my pet turtle to draw it! (enter to continue) ")

# create a dictionary of turtle colours
# start with a list of colours that turle recognises
turtle_colours = ["red", "green", "yellow", "blue", "purple", "cyan"]

# now use zip to make the DICTIONARY of colours
# [🧑‍💻 YOUR CODE HERE]

# uncomment all of the code below before you start
# # TURTLE SETUP
# screen = turtle.Screen()
# screen.setup(1.0, 1.0)

# t = turtle.Turtle()
# t.shape("turtle")
# t.up()
# t.setpos(-50, -100)
# t.down()

# # 🐢 draw the polygon in turtle
# # lookup the correct colour
# turtle_colour = "[🧑‍💻 YOUR CODE HERE]"

# # change the colour of the turtle
# t.fillcolor(turtle_colour)

# # tell turtle to start filling in the colour
# t.begin_fill()

# # use a for loop to get turtle to draw the correct shape, in the correct colour!
# # [🧑‍💻 YOUR CODE HERE]
    
# # tell turtle to stop filling in the colour
# t.end_fill()

# # code needed at the end to keep turtle running
# screen.mainloop()