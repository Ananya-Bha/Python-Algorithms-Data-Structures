#TITLE : Who wants to become a Millionaire?
#COMPONENTS OF THE GAME
#LIBRAIRIES:
#time
#turtle
#VARIABLES:
#answer - stores users input for if/else statements
#money - stores the amount of money the user has
#elapsed_time - stores the amount of time the user has left to      answer a question
#choice - stores the users choice of answer in choice()
#FUNCTIONS:
#1.Main() Function - this is the function that starts the game      and gives a basic introduction to the game
#2.Choice() Function - the main function calls this function to     ask the user if they are ready to play the game
#3.Rules() Function - the choice function call this function to     show the user the rules of the game
#4.start() function - is called by the rules function to begin      the game. It sets up the turtle timer and calls the next            function
#5.Q1() function - this function is called by the start             function to ask the first question, start the timer and call        the next function based on the users input
#6. Q2(),Q3(),Q4(),Q5() functions: these functions are called       one after another, they contain the timers for each of the          questions and the next function is called based on the users        input
#7.complete() function - this function is called when the user       answers the last question correctly and the game ends,              making them win a million dollars
#8.incorrect() function - this function is called when the user      answers the last question incorrectly and the game ends
#-----------------------------------------------------------------#
#-----------------------------------------------------------------#

#Import Time & Turtle Libraries

#define incorrect()
#print("Incorrect! You lose!")
#print("You won $",money)
#print("GAME OVER")

#define complete()
#tell user they have completed the game and have won 1 million      dollars
#game stops

#define Q5()
#display questions and answers
#wait for 5 seconds
#start timer(20 secs) and inform user of time left
#if/elif/else statement to check if user input is correct
#if correct and elapsed_time<20, call complete()
#else call incorrect()

#define Q4()
#display questions and answers
#wait for 5 seconds
#start timer(15 secs) and inform user of time left
#if/elif/else statement to check if user input is correct
#if correct and elapsed_time<15, call Q5()
#else call incorrect()

#define Q3()
#display questions and answers
#wait for 5 seconds
#start timer(15 secs) and inform user of time left
#if/elif/else statement to check if user input is correct
#if correct and elapsed_time<15, call Q4()
#else call incorrect()

#define Q2()
#display questions and answers
#wait for 5 seconds
#start timer(10 secs) and inform user of time left
#if/elif/else statement to check if user input is correct
#if correct and elapsed_time<10, call Q3()
#else call incorrect()

#define Q1()


def Q2():
  print("")


#define start()
def start():
  import time
  import turtle as t
  money = 0
  print(
      "Great! Lets Begin ...\nTurtle is setting up the timer for you!\nOnce the screen is set up you will be shown your first Question, be prepared🔍🔍"
  )
  #import Turtle library
  import turtle as t
  import time
  #setup turtle screen
  #create a screen
  screen = t.Screen()
  screen.title("Turtle Clock Timer")
  screen.setup(width=550, height=420)

  #create and position turtles
  clone = t.Turtle()
  clone.hideturtle()
  t = t.Turtle()
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
  #show question details
  print(
      "The screen is set up!\nYour first Question (if answered correctly) has a chance to win you $1000!\n\n-----HERE ARE THE QUESTION DETAILS-----\nQUESTION: 1\nDIFFICULTY: Easy\nPRIZE MONEY: $1000\nCURRENT BALANCE: $",
      money,
      "\nTIME TO ANSWER QUESTION: 10 seconds\n---------------------------------------"
  )

  #display questions and answers
  print("Your time starts now!")
  print(
      "Q1) In a website browser address bar, what does “www” stand for?\n\nA) World Wide Web\nB) World Wide Wares\nC) World Wide War\nD) World Wide Waste"
  )
  print("You have 5 seconds to read the question!")
  time.sleep(5)
  
  #start timer(10 secs) and inform user of time left
  #start time tracking
  start_time = time.time()
  elapsed_time = 0
  #set turtle size & colour for tracking
  t.pensize(5)
  t.shape("arrow")
  t.color("yellow")

  #start Time loop for 10 seconds
  if elapsed_time < 10:
    while answer := input("Enter your answer: "):
      #move turtle forward
      t.forward(0.5)
      t.speed(1)
      #update elapsed time
      elapsed_time = time.time() - start_time  # Elapsed time since the start
      # Clear and update the time display at the top
      clone.clear()
      clone.write(f"Time: {int(elapsed_time)} seconds",
                  align="center",
                  font=("Arial", 12, "normal"))
      if answer.lower() == "a" and elapsed_time < 10:
        print(
            "Correct! You have won $1000!\nYou can now move onto the next Question!🥳🥳🥳🥳"
        )
        money += 1000
        Q2()
        break
      elif elapsed_time >= 10:
        print("Incorrect! You lose!")
        break

    #if/elif/else statement to check if user input is correct\
      
    #if correct and elapsed_time<10, call Q2()
    #else call incorrect()
      
  
  
  


#-----------------------------------------------------------------#


#define rules()
def rules():
  #print rules of the game
  print("\n\n🎯🎯🎯🎯🎯🎯🎯🎯THESE ARE THE RULES OF THE GAME🎯🎯🎯🎯🎯🎯🎯🎯\n\n")
  print(
      "1.  Parcipants will be asked a series of 5 questions, each with four possible answers.\n2.  A timer will start 5 seconds after the question is asked and the user will have a certain amount of time to answer the question based on its difficulty.\n3.  If the user answers the question correctly, they move onto the next question with their prize money increasing.\n4.  If the user answers the question incorrectly or their time to answer the question runs out, the game ends and they lose.\n5.  At Question 3 you will be shown your 'safe haven'  which will guarantee you a certain amount of money to take home(even if you answer further questions incorrectly) if answered correctly.\n6.  If you answer all 5 questions correctly, you win the game and are a Millionaire!\n7.  Remember to HAVE FUN ,Good Luck & Enjoy !\n\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯\n\n"
  )
  rules = input("Have you read the rules? (y/n):")
  if rules.lower() == "y":
    start()
  elif rules.lower() == "n":
    print("Too bad! The game is starting anyways!")
    start()
  else:
    print("Invalid Input! Please try again!")

  #call start()


#-----------------------------------------------------------------#


#define choice()
def choice():
  #ask user if they are ready to play the game
  choice = input(
      "Are you ready to play 'Who Wants to Be a Millionaire?'(yes/no):")
  #if yes, call rules()
  if choice.lower() == "yes":
    rules()
  #else, print("Okay, maybe next time!")
  elif choice.lower() == "no":
    print("\n\nOkay, maybe next time!👋🏼👋🏼👋🏼\nSee you later alligator🐊...")
  #else, print("Invalid Input! Please enter yes or no next time!.")
  else:
    print("\n\nInvalid Input!😠😠😠 Please enter yes or no next time!.")


#-----------------------------------------------------------------#


#define main()
def main():
  #introduction
  print("💵💸💰🤑WHO WANTS TO BE A MILLIONAIRE?🤑💰💸💵")
  print(
      "Your Journey to Fortune Begins Here!\n\nWelcome to Who Wants to be a Millionaire?\n-----------------------------------------------------------------\nBASIC INTRODUCTION:\n--> Who Wants to Be a Millionaire? is a quiz show in which participants must accurately answer a sequence of multiple-choice questions to progress to the next level.\n--> The game consists of 5 questions, each assigned a specific monetary value, with a time limit for contestants to formulate their answers.\n-----------------------------------------------------------------\n"
  )
  #call choice()
  choice()


#call main()
main()
