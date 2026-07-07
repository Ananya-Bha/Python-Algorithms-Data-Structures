#10 second timer
'''
#import libraries
import time 
import turtle as t

#create a screen
screen = t.Screen()
screen.title("Turtle Clock Timer")
screen.setup(width=550, height=420)

#create and position turtles
clone=t.Turtle()
clone.hideturtle()
t=t.Turtle()
t.setheading(90)
t.penup()
t.forward(50)
t.pendown()

#draw time scale
t.left(90)
t.forward(100)
t.left(90)
t.forward(30)
t.left(90)
t.forward(200)
t.left(90)
t.forward(30)
t.left(90)
t.forward(200)

#draw time marks
t.left(90)
t.color("black")
t.forward(20)
t.backward(20)
t.left(90)
for i in range(9):
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.backward(10)
  t.left(90)
t.forward(10)
t.right(90)
t.color("green")
t.forward(20)
t.backward(20)
t.left(90)
for i in range(4):
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.backward(10)
  t.left(90)
t.forward(10)
t.right(90)
t.color("blue")
t.forward(20)
t.backward(20)
t.left(90)
for i in range(4):
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.backward(10)
  t.left(90)
t.forward(10)
t.right(90)
t.color("red")
t.forward(20)
t.backward(20)
t.right(90)

# return to start of box 
t.penup()
t.forward(200)
t.left(180)
t.pendown()
t.pensize(5)
t.shape("arrow")
t.color("yellow")

#start time tracking
start_time=time.time()
elapsed_time=0
  #set turtle size & colour for tracking
t.pensize(5)
t.shape("arrow")
t.color("yellow")

#start Time loop for 10 seconds
while elapsed_time<10:
  #move turtle forward
  t.forward(0.5)
  t.speed(1)
  #update elapsed time
  elapsed_time = time.time() - start_time  # Elapsed time since the start
  # Clear and update the time display at the top
  clone.clear()
  clone.write(f"Time: {int(elapsed_time)} seconds",     align="center", font=("Arial", 16, "normal"))

# End the timer and print the final time
print("Timer has reached 10 seconds!")
print("Your time is up!❌")

time.sleep(100)
'''
  
#15 second timer 
'''
#import libraries
import time 
import turtle as t

#create a screen
screen = t.Screen()
screen.title("Turtle Clock Timer")
screen.setup(width=550, height=420)

#create and position turtles
clone=t.Turtle()
clone.hideturtle()
t=t.Turtle()
t.setheading(90)
t.penup()
t.forward(50)
t.pendown()

#draw time scale
t.left(90)
t.forward(100)
t.left(90)
t.forward(30)
t.left(90)
t.forward(200)
t.left(90)
t.forward(30)
t.left(90)
t.forward(200)

#draw time marks
t.left(90)
t.color("black")
t.forward(20)
t.backward(20)
t.left(90)
for i in range(9):
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.backward(10)
  t.left(90)
t.forward(10)
t.right(90)
t.color("green")
t.forward(20)
t.backward(20)
t.left(90)
for i in range(4):
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.backward(10)
  t.left(90)
t.forward(10)
t.right(90)
t.color("blue")
t.forward(20)
t.backward(20)
t.left(90)
for i in range(4):
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.backward(10)
  t.left(90)
t.forward(10)
t.right(90)
t.color("red")
t.forward(20)
t.backward(20)
t.right(90)

# return to start of box 
t.penup()
t.forward(200)
t.left(180)
t.pendown()
t.pensize(5)
t.shape("arrow")
t.color("yellow")

#start time tracking
start_time=time.time()
elapsed_time=0
  #set turtle size & colour for tracking
t.pensize(5)
t.shape("arrow")
t.color("yellow")

#start Time loop for 10 seconds
while elapsed_time<15:
  #move turtle forward
  t.forward(0.5)
  t.speed(1)
  #update elapsed time
  elapsed_time = time.time() - start_time  # Elapsed time since the start
  # Clear and update the time display at the top
  clone.clear()
  clone.write(f"Time: {int(elapsed_time)} seconds",     align="center", font=("Arial", 12, "normal"))

# End the timer and print the final time
print("Timer has reached 15 seconds!")
print("Your time is up!❌")

time.sleep(100)
'''
'''
#20 second timer
#15 second timer  
#import libraries
import time 
import turtle as t

#create a screen
screen = t.Screen()
screen.title("Turtle Clock Timer")
screen.setup(width=550, height=420)

#create and position turtles
clone=t.Turtle()
clone.hideturtle()
t=t.Turtle()
t.setheading(90)
t.penup()
t.forward(50)
t.pendown()

#draw time scale
t.left(90)
t.forward(100)
t.left(90)
t.forward(30)
t.left(90)
t.forward(200)
t.left(90)
t.forward(30)
t.left(90)
t.forward(200)

#draw time marks
t.left(90)
t.color("black")
t.forward(20)
t.backward(20)
t.left(90)
for i in range(9):
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.backward(10)
  t.left(90)
t.forward(10)
t.right(90)
t.color("green")
t.forward(20)
t.backward(20)
t.left(90)
for i in range(4):
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.backward(10)
  t.left(90)
t.forward(10)
t.right(90)
t.color("blue")
t.forward(20)
t.backward(20)
t.left(90)
for i in range(4):
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.backward(10)
  t.left(90)
t.forward(10)
t.right(90)
t.color("red")
t.forward(20)
t.backward(20)
t.right(90)

# return to start of box 
t.penup()
t.forward(200)
t.left(180)
t.pendown()
t.pensize(5)
t.shape("arrow")
t.color("yellow")

#start time tracking
start_time=time.time()
elapsed_time=0
  #set turtle size & colour for tracking
t.pensize(5)
t.shape("arrow")
t.color("yellow")

#start Time loop for 10 seconds
while elapsed_time<20:
  #move turtle forward
  t.forward(0.5)
  t.speed(1)
  #update elapsed time
  elapsed_time = time.time() - start_time  # Elapsed time since the start
  # Clear and update the time display at the top
  clone.clear()
  clone.write(f"Time: {int(elapsed_time)} seconds",     align="center", font=("Arial", 12, "normal"))

# End the timer and print the final time
print("Timer has reached 20 seconds!")
print("Your time is up!❌")

time.sleep(100)

'''
'''
#Title: Who wants to become a millionaire?
import time as time 
import turtle as t

def question1():
  print('hello')

def timer_setup():
  print("Turtle will now draw you Timer on the screen!\nRemember:\n 1.The timer will start 5 seconds after you recieve your question\n 2.The yellow arrow at the top of the scale indicates how much time has gone by in seconds\n 3.The green arrow indicate 10 seconds\n  .The blue arrow indicates 15 seconds\n  .The red arrow indicates 20 seconds\n  .If you answer the question incorrectly the game will end and unfortuanately you weren't able to become a millionaire\n 3.If you answer the question correctly you will move on to the next question\n 4.If you run out of time to answer the questions or answer it incorrectly ,you will unfortuanately lose all you money and the game will end\n ")


  #create a screen
  screen = t.Screen()
  screen.title("Turtle Clock Timer")
  screen.setup(width=550, height=420)

  #create and position turtles
  clone=t.Turtle()
  clone.hideturtle()
  t=t.Turtle()
  t.setheading(90)
  t.penup()
  t.forward(50)
  t.pendown()

  #draw time scale
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(30)
  t.left(90)
  t.forward(200)
  t.left(90)
  t.forward(30)
  t.left(90)
  t.forward(200)

  #draw time marks
  t.left(90)
  t.color("black")
  t.forward(20)
  t.backward(20)
  t.left(90)
  for i in range(9):
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.backward(10)
    t.left(90)
  t.forward(10)
  t.right(90)
  t.color("green")
  t.forward(20)
  t.backward(20)
  t.left(90)
  for i in range(4):
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.backward(10)
    t.left(90)
  t.forward(10)
  t.right(90)
  t.color("blue")
  t.forward(20)
  t.backward(20)
  t.left(90)
  for i in range(4):
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.backward(10)
    t.left(90)
  t.forward(10)
  t.right(90)
  t.color("red")
  t.forward(20)
  t.backward(20)
  t.right(90)

  # return to start of box 
  t.penup()
  t.forward(200)
  t.left(180)
  t.pendown()
  t.pensize(5)
  t.shape("arrow")
  t.color("yellow")
  
  
#start function
def start():
  print("\n💰💰💰💰💰💰💰💰💰Let's Begin!💰💰💰💰💰💰💰💰💰\n")
  timer_setup()
  question1()
  

#rules function
def rules():
  print("\n\n💵💶💷💴THESE ARE THE RULES OF THE GAME💴💷💶💵\nPlease read them carefully\n")
  print("1.Contestants respond to a series of multiple-choice questions, with each correct answer raising the prize money.\n2.The game ends when a contestant answers a question incorrectly, or when the contestant runs out of time.\n3.There are designated 'milestone levels' that ensure a guaranteed sum of money once a contestant reaches those specific questions.\n4.You will need to answer a total of 9 questions. \n5.At questions 3 and 6, you will be shown your ‘milestone money’ which you can recieve by providing correct answers to the presented questions.\n\n💴💷💶💵LIFELINE RULES:💴💷💶💵\n1.You will be given 2 lifelines to help you out. \n2.The first lifeline is 50:50, which allows you to remove 2 incorrect answers from the options given.\n3.The second lifeline is a hint, which reveals a hint about the answer to your question\n\n--PS: You will only be able to use each lifeline once so choose wisely...🔎🔎🔎🔎--")
  start()

#choice function
def choice():
  choice=input("Do you want to play the game? (yes/no): ")
  choice=choice.lower()
  if choice=="yes":
    rules()
  elif choice=="no":
    print("\nThank you for visiting!\nSee you later...👋👋👋👋👋👋")
  else:
    print("Invalid input. Please try again.\n😠😠😠😠😠😠😠😠😠😠😠😠\n\n")
    

# main function
def main():
  #import libraries
  

  print("💵💸💰🤑WHO WANTS TO BE A MILLIONAIRE?🤑💰💸💵")
  print("Welcome to Who Wants to be a Millionaire? Your Journey to Fortune Begins Here!\n-----------------------------\nBASIC INTRODUCTION:\n--> Who Wants to Be a Millionaire? is a quiz show in which participants must accurately answer a sequence of multiple-choice questions to progress to the next level.\n--> The game consists of 9 questions, each assigned a specific monetary value, with a time limit for contestants to formulate their answers.\n-->Additionally, contestants are provided with two Lifelines to help them if they encounter difficulties with a question.\n--------------------\n")
  choice()

main()

t.done()
'''
'''
time.sleep(5)
#start timer(10 secs) and inform user of time left
#start time tracking
start_time=time.time()
elapsed_time=0
  #set turtle size & colour for tracking
t.pensize(5)
t.shape("arrow")
t.color("yellow")

#start Time loop for 10 seconds
while elapsed_time<10:
  #move turtle forward
  t.forward(0.5)
  t.speed(1)
  #update elapsed time
  elapsed_time = time.time() - start_time  # Elapsed time since the start
  # Clear and update the time display at the top
  clone.clear()
  clone.write(f"Time: {int(elapsed_time)} seconds",     align="center", font=("Arial", 12, "normal"))
  if answer.lower()== "a" and elapsed_time<10:
    print("Correct! You have won $1000!\nYou can now move onto the next Question!🥳🥳🥳🥳")
    money+=1000
    break

  elif  elapsed_time>=10:
    print("Incorrect! You lose!")
    break
  #if correct and elapsed_time<10, call Q2()
  #else call incorrect()
#if/elif/else statement to check if user input is correct\
'''


import time 
import turtle as t
time.sleep(5)
#start timer(10 secs) and inform user of time left
#start time tracking
start_time=time.time()
elapsed_time=0
  #set turtle size & colour for tracking
t.pensize(5)
t.shape("arrow")
t.color("yellow")

while elapsed_time<10:
  #move turtle forward
  t.forward(0.5)
  t.speed(1)
  
