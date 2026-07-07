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
my_dictionary = {}
'''
"polygon":f"A flat shape with {bold}{underline}straight sides{reset}. Think of it like a drawing made by connecting dots with straight lines.","vertex":f"The corners or points {bold}{underline}where the sides of a polygon meet{reset}. If you draw a shape, the sharp corners where the lines end are the vertices.","side":"idk"
'''

# print(type(my_dictionary))
# print(my_dictionary)
# print(my_dictionary.get("polygon",))

# -------------------------------------------------
# CHALLENGE 2 - UPDATING THE DICTIONARY
# -------------------------------------------------

# add one new entry to the dictionary using square brackets
"""
3. side
{underline}.
"""
# [🧑‍💻 YOUR CODE HERE]
'''
my_dictionary["side"]="The thing Deleted but it talked about sides"
'''

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
polygons = {"Triangle":f"A polygon with {g} three sides.{reset}"
,"Quadrilateral":f"A polygon with {b}four sides.{reset}","Pentagon":f"A polygon with {p}five sides.{reset}","Hexagon":f"A polygon with {y}six sides.{reset}","Heptagon":f"A polygon with{c} seven sides.{reset}","Octagon":f"A polygon with {w}{bold}eight sides.{reset}"}
list_shape_name=list(polygons.keys())
list_shape_meaning=list(polygons.values())
final= dict(zip(list_shape_name,list_shape_meaning))

# update your original dictionary with this new dictionary
my_dictionary.update(polygons)

# -------------------------------------------------
# CHALLENGE 3 - DICTIONARY FORMATTING
# -------------------------------------------------


# keep asking the user for a word to look up until they quit
# then output that word and its meaning to the console
# 🚀 BONUS! Format the output nicely with text styles, white space etc.
'''
while True:
    word = input("Which word should I look up? (q to quit) ")
    word=word.lower()
    if word == "q":
        break
    else:
        output = my_dictionary.get(word)
        print(output)
'''

# ===========================================================
# 2️⃣ LESSON 9.4 DICTIONARIES II
# ===========================================================

# -------------------------------------------------
# CHALLENGE 4 - KEYS AND VALUES FROM DICTIONARIES
# -------------------------------------------------

# get a LIST of polygon names from the dictionary without retyping them
polygons= list(my_dictionary.keys())
print(polygons)
# iterate through the list and print each polygon on a separate line
# uncomment the code below before you start
# print("\nPOLYGONS")
# # [🧑‍💻 YOUR CODE HERE]
print("\nPOLYGONS:")
for polygon in polygons:
    print(polygon)

# # get a LIST of definitions of each polygon from the dictionary
# # [🧑‍💻 YOUR CODE HERE]
definitions=list(my_dictionary.values())
print("\nDEFINITIONS:")
for definition in definitions:
    print(definition)
print("\n")

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
my_dictionarey2={"3":"Triangle","4":"Quadrilateral","5":"Pentagon","6":"Hexagon","7":"Heptagon","8":"Octagon"}
list1=list(my_dictionarey2.keys())
list2=list(my_dictionarey2.values())
new= dict(zip(list1,list2))
print(new)
# print it to see that it's a dictionary
# uncomment the line below before you start
# print("\nDICTIONARY")
# [🧑‍💻 YOUR CODE HERE]

# choose a random number of sides from the list
num = random.choice(list1)

# lookup and print the matching POLYGON NAME
shape= my_dictionarey2[num]
print(num,shape)

# lookup and print the matching DEFINITION for that polygon
# [🧑‍💻 YOUR CODE HERE]
definition= my_dictionary[shape]
print(definition)
# -------------------------------------------------
# CHALLENGE 6 - EXTERNAL ANGLES OF POLYGONS
# -------------------------------------------------
# create an empty dictionary
external_angles= {}
side= list(external_angles.keys())
ex_angle = list(external_angles.values())
external_angles=dict(zip(side,ex_angle))
# calculate the internal angles for each number of sides
for num_sides in sides_list:
    # calculate the size of the external angle
    angle = round(360 / num_sides, 1)
    # add the number of sides and angle to the dictionary
    side.append(num_sides)
    ex_angle.append(angle)
    external_angles.update(zip(side,ex_angle))

# print the dictionary, just to check your output
print(f"\n{c}Challenge 6:{reset}\n",external_angles)

# -------------------------------------------------
# CHALLENGE 7 - DICTIONARIES WITH THE SAME KEYS
# -------------------------------------------------

# make multiple dictionaries using the same keys
console_colours = [r, g, y, b, p, c]
colours={}
colours=dict(zip(sides_list,console_colours))
emojis={}
number_emojis={}
# this is a list of VARIABLES, containing ANSI escape codes from the top of the script


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