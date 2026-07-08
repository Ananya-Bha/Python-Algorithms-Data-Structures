import os
import webbrowser
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


#1.List Variables:
Yellow_collar=0
Black_collar=0
Brown_collar=0
Red_collar=0
Green_collar=0
White_collar=0
Pink_collar=0
Blue_collar=0

#2.Set up functions for adding a point to each collar job

def add_1_yellow_collar():
  global Yellow_collar
  Yellow_collar+=1

def add_1_black_collar():
  global Black_collar
  Black_collar+=1

def add_1_brown_collar():
  global Brown_collar
  Brown_collar+=1

def add_1_red_collar():
  global Red_collar
  Red_collar+=1

def add_1_white_collar():
  global White_collar
  White_collar+=1

def add_1_pink_collar():
  global Pink_collar
  Pink_collar+=1

def add_1_blue_collar():
  global Blue_collar
  Blue_collar+=1

def add_1_green_collar():
  global Green_collar
  Green_collar+=1

#3.Create a function for each Description for each collar

def des_Blcollar():
  ask= input(f"\nWould you like to open a website which talks about {b}Blue{reset} Collar Jobs? (yes or no):")
  if ask.lower() =="yes":
    url ="http://127.0.0.1:5500/Blue_Collar/index.html"
    webbrowser.open(url)
  else :
    print("No problem! Incase you would like to visit the webite later here is the link:\nhttp://127.0.0.1:5500/Blue_Collar/index.html")


def des_Bkcollar():
  ask= input(f"\nWould you like to open a website which talks about{k} Black{reset} Collar Jobs? (yes or no):")
  if ask.lower() =="yes":
    url="https://drive.google.com/file/d/11jTc7UJJ71Ohdc5k0P4cS1b6jxJIynom/view?usp=drive_link"
    webbrowser.open(url)
  else :
    print("No problem! Incase you would like to visit the webite later here is the link:\nhttp://127.0.0.1:5500/Black_Collar/index.html")

def des_Brcollar():
  ask= input(f"\nWould you like to open a website which talks about {bold}Brown{reset} Collar Jobs? (yes or no):")
  if ask.lower() =="yes":
    url ="http://127.0.0.1:5500/Brown_Collar/index.html"
    webbrowser.open(url)
  else :
    print("No problem! Incase you would like to visit the webite later here is the link:\nhttp://127.0.0.1:5500/Brown_Collar/index.html")


def des_Pcollar():
  ask= input(f"\nWould you like to open a website which talks about{p} Pink Collar{reset} Jobs? (yes or no):")
  if ask.lower() =="yes":
    url ="http://127.0.0.1:5500/Pink_Collar/index.html"
    webbrowser.open(url)
  else :
    print("No problem! Incase you would like to visit the webite later here is the link:\nhttp://127.0.0.1:5500/Pink_Collar/index.html")


def des_Rcollar():
  ask= input(f"\nWould you like to open a website which talks about {r}Red{reset} Collar Jobs? (yes or no):")
  if ask.lower() =="yes":
    url ="http://127.0.0.1:5500/Red_Collar/index.html"
    webbrowser.open(url)
  else :
    print("No problem! Incase you would like to visit the webite later here is the link:\nhttp://127.0.0.1:5500/Red_Collar/index.html")


def des_Ycollar():
  ask= input(f"\nWould you like to open a website which talks about{y} Yellow{reset} Collar Jobs? (yes or no):")
  if ask.lower() =="yes":
    url ="http://127.0.0.1:5500/Yellow_Collar/index.html"
    webbrowser.open(url)
  else :
    print("No problem! Incase you would like to visit the webite later here is the link:\nhttp://127.0.0.1:5500/Yellow_Collar/index.html")


def des_Gcollar():
  ask= input(f"\nWould you like to open a website which talks about{g} Green Collar{reset} Jobs? (yes or no):")
  if ask.lower() =="yes":
    url ="http://127.0.0.1:5500/Green_Collar/index.html"
    webbrowser.open(url)
  else :
    print("No problem! Incase you would like to visit the webite later here is the link:\nhttp://127.0.0.1:5500/Green_Collar/index.html")

def des_Wcollar():
  ask= input(f"\nWould you like to open a website which talks about {underline}White{reset} Collar Jobs? (yes or no):")
  if ask.lower() =="yes":
    url ="http://127.0.0.1:5500/White_Collar/index.html"
    webbrowser.open(url)
  else :
    print("No problem! Incase you would like to visit the webite later here is the link:\nhttp://127.0.0.1:5500/White_Collar/index.html")


#4.Set up other functions for quick use
def final_result():
  # Create a dictionary to store collar names and their values
  collars = {
    "Yellow": Yellow_collar,
    "Black": Black_collar,
    "Brown": Brown_collar,
    "Red": Red_collar,
    "Green": Green_collar,
    "White": White_collar,
    "Pink": Pink_collar,
    "Blue": Blue_collar
  }

  # Find the collar with maximum points
  max_collar = max(collars.items(), key=lambda x: x[1])

  print(f"------------------------------------------------------------------------\n{r}The collar with the highest points is: {max_collar[0]} Collar with {max_collar[1]} points!{reset}\n------------------------------------------------------------------------\n")
  # Print specific message based on the winning collar
  if max_collar[0] == "Blue":
    print(f"{bold}You are best suited for hands-on, manual labor roles!{reset}")
    des_Blcollar()
  elif max_collar[0] == "White":
    print(f"{bold}{underline}You are best suited for professional and office-based roles!{reset}")
    des_Wcollar()
  elif max_collar[0] == "Pink":
    print(f"{bold}{underline}You are best suited for care-oriented and service positions!{reset}")
    des_Pcollar()
  elif max_collar[0] == "Green":
    print(f"{bold}{underline}You are best suited for environmental and sustainability focused work!{reset}")
    des_Gcollar()
  elif max_collar[0] == "Yellow":
    print(f"{bold}{underline}You are best suited for creative and artistic roles!{reset}")
    des_Ycollar()
  elif max_collar[0] == "Red":
    print(f"{bold}{underline}You are best suited for government and public service positions!{reset}")
    des_Rcollar()
  elif max_collar[0] == "Black":
    print(f"{bold}{underline}You are best suited for mining and resource extraction industries!{reset}")
    des_Bkcollar()
  elif max_collar[0] == "Brown":
    print(f"{bold}{underline}You are best suited for military and law enforcement roles!{reset}")
    des_Brcollar()





def calculation():
  os.system("clear")
  print(f"------------------------------------------------------------------------\n{bold}{r}{underline}Here are your final calculations for the number of points earned by each collar job:{reset}\n------------------------------------------------------------------------\n")
  print("Red Collar:",Red_collar)
  print("Green Collar:",Green_collar)
  print("Blue Collar:",Blue_collar)
  print("Black Collar:",Black_collar)
  print("Brown Collar:",Brown_collar)
  print("Pink Collar:",Pink_collar)
  print("Yellow Collar:",Yellow_collar)
  print("White Collar:",White_collar)
  final_result()
#6.Start asking questions

def Q20():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}20{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Do you enjoy work that revolves around eco-friendly tech?{reset} \na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_green_collar()
    print("The Quiz has finished! You will be directed to a new page!")
    calculation()
  elif user_choice.lower()=="b":
    add_1_brown_collar()
    add_1_blue_collar()
    add_1_black_collar()
    add_1_pink_collar()
    add_1_white_collar()
    add_1_yellow_collar()
    add_1_red_collar()
    print("The Quiz has finished! You will be directed to a new page!")
    calculation()

def Q19():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}19{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Do you like technical jobs ?{reset}  \na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_green_collar()
    Q20()
  elif user_choice.lower()=="b":
    add_1_brown_collar()
    add_1_blue_collar()
    add_1_black_collar()
    add_1_pink_collar()
    add_1_white_collar()
    add_1_yellow_collar()
    add_1_red_collar()
    Q20()

def Q18():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}18{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Do you enjoy helping the environment? {reset}\na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_green_collar()
    Q19()
  elif user_choice.lower()=="b":
    add_1_brown_collar()
    add_1_blue_collar()
    add_1_black_collar()
    add_1_pink_collar()
    add_1_white_collar()
    add_1_yellow_collar()
    add_1_red_collar()
    Q19()

def Q17():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}17{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Would you like being a part of a system that influences society ?{reset} \na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_red_collar()
    Q18()
  elif user_choice.lower()=="b":
    add_1_brown_collar()
    add_1_blue_collar()
    add_1_black_collar()
    add_1_pink_collar()
    add_1_white_collar()
    add_1_yellow_collar()
    add_1_green_collar()
    Q18()

def Q16():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}16{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Are you okay with working under strict policies?{reset} \na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_red_collar()
    add_1_white_collar()
    Q17()
  elif user_choice.lower()=="b":
    add_1_blue_collar()
    add_1_brown_collar()
    add_1_black_collar()
    add_1_yellow_collar()
    add_1_pink_collar()
    add_1_green_collar()
    Q17()

def Q15():
  print(f"\n⭕{r}------------------------------------{reset}⭕-\n\nQuestion Number {underline}{bold}15{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Are you okay with working for the government and public companies?{reset} \na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_red_collar()
    Q16()
  elif user_choice.lower()=="b":
    add_1_brown_collar()
    add_1_blue_collar()
    add_1_black_collar()
    add_1_pink_collar()
    add_1_white_collar()
    add_1_yellow_collar()
    add_1_green_collar()
    Q16()

def Q14():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}14{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Are you okay with following rules or orders given by other people?{reset}\na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_brown_collar()
    Q15()
  elif user_choice.lower()=="b":
    add_1_blue_collar()
    add_1_black_collar()
    add_1_pink_collar()
    add_1_red_collar()
    add_1_white_collar()
    add_1_yellow_collar()
    add_1_green_collar()
    Q15()

def Q13():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}13{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Can you stay calm,efficient and fast in stressful situations?{reset}\na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_brown_collar()
    add_1_red_collar()
    add_1_white_collar()
    add_1_pink_collar()
    Q14()
  elif user_choice.lower()=="b":
    add_1_blue_collar()
    add_1_black_collar()
    add_1_yellow_collar()
    add_1_green_collar()
    Q14()

def Q12():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}12{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Do you enjoy being outside ?{reset} \na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_black_collar()
    add_1_green_collar()
    Q13()
  elif user_choice.lower()=="b":
    add_1_blue_collar()
    add_1_brown_collar()
    add_1_yellow_collar()
    add_1_red_collar()
    add_1_pink_collar()
    add_1_white_collar()
    Q13()

def Q11():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}11{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Can you handle working in a harsh environment?{reset} \na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_black_collar()
    Q12()
  elif user_choice.lower()=="b":
    add_1_brown_collar()
    add_1_green_collar()
    add_1_pink_collar()
    add_1_red_collar()
    add_1_white_collar()
    add_1_blue_collar()
    add_1_yellow_collar()
    Q12()

def Q10():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}10{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Do you have passions for the arts ?{reset}  \na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_yellow_collar()
    Q11()
  elif user_choice.lower()=="b":
    add_1_blue_collar()
    add_1_black_collar()
    add_1_brown_collar()
    add_1_green_collar()
    add_1_pink_collar()
    add_1_red_collar()
    add_1_white_collar()
    Q11()

def Q9():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}9{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Do you enjoy having a flexible schedule?{reset} \na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_yellow_collar()
    Q10()
  elif user_choice.lower()=="b":
    add_1_blue_collar()
    add_1_black_collar()
    add_1_brown_collar()
    add_1_green_collar()
    add_1_pink_collar()
    add_1_red_collar()
    add_1_white_collar()
    Q10()

def Q8():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}8{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Are you well educated ?{reset}\na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_white_collar()
    add_1_pink_collar()
    add_1_red_collar()
    add_1_green_collar()
    Q9()
  elif user_choice.lower()=="b":
    add_1_black_collar()
    add_1_blue_collar()
    add_1_brown_collar()
    add_1_yellow_collar()
    Q9()

def Q7():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}7{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Are you good with working with people?{reset}\na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_blue_collar()
    add_1_pink_collar()
    add_1_brown_collar()
    add_1_red_collar()
    add_1_white_collar()
    Q8()
  elif user_choice.lower()=="b":
    add_1_green_collar()
    add_1_black_collar()
    add_1_yellow_collar()
    Q8()

def Q6():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}6{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Can you handle irregular schedules?{reset}\na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_yellow_collar()
    add_1_brown_collar()
    add_1_black_collar()
    add_1_white_collar()
    Q7()
  elif user_choice.lower()=="b":
    add_1_pink_collar()
    add_1_green_collar()
    add_1_red_collar()
    add_1_blue_collar()
    Q7()

def Q5():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}5{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Do you enjoy doing manual labour?{reset}\na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_black_collar()
    add_1_blue_collar()
    add_1_brown_collar()
    Q6()
  elif user_choice.lower()=="b":
    add_1_pink_collar()
    add_1_yellow_collar()
    add_1_white_collar()
    add_1_green_collar()
    Q6()

def Q4():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}4{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Are you creative?{reset}\na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_yellow_collar()
    Q5()
  elif user_choice.lower()=="b":
    add_1_blue_collar()
    add_1_black_collar()
    add_1_brown_collar()
    add_1_pink_collar()
    add_1_red_collar()
    add_1_white_collar()
    add_1_green_collar()
    Q5()

def Q3():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}3{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Do you enjoy serving people(protecting ,helping,entertaining)?{reset}\na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_brown_collar()
    add_1_pink_collar()
    add_1_white_collar()
    add_1_red_collar()
    add_1_yellow_collar()
    Q4()
  elif user_choice.lower()=="b":
    add_1_black_collar()
    add_1_green_collar()
    add_1_blue_collar() 
    Q4()

def Q2():
  print(f"\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}2{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Do you consider yourself quite patient ?{reset}\na) Yes\nb) No")
  user_choice= input("Enter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_blue_collar()
    add_1_pink_collar()
    add_1_brown_collar()
    add_1_red_collar()
    add_1_white_collar()
    Q3()
  elif user_choice.lower()=="b":
    add_1_yellow_collar()
    add_1_black_collar()
    add_1_pink_collar()
    Q3()

def Q1():
  print(f"{underline}{bold}Great! Let's get started...{reset}\n\n⭕{r}------------------------------------{reset}⭕\n\nQuestion Number {underline}{bold}1{reset} of {underline}{bold}20{reset}\n{underline}{bold}Question:Do you think you are disciplined ?{reset}\na) Yes\nb) No")
  user_choice= input("\nEnter your answer here (a or b):")
  if user_choice.lower()=="a":
    add_1_blue_collar()
    add_1_black_collar()
    add_1_brown_collar()
    add_1_red_collar()
    Q2()
  elif user_choice.lower()=="b":
    add_1_yellow_collar()
    add_1_green_collar()
    add_1_white_collar()
    add_1_pink_collar()
    Q2()


#Introduction
def SDG_8():
  print(f"This project is based on SDG 8, {bold}{r}Decent Work and Economic Growth.{reset}\n➡️  This SDG aims to promote inclusive and sustainable economic growth, full and productive employment, and decent work for all.\n➡️  It focuses on ensuring that everyone has access to fair job opportunities, safe working conditions, and the ability to earn a living wage.\n\n{bold}-------------------------------------------------------------------------------{reset}")
def connection():
  print(f"\n{w}{underline}{bold}1.Connection to our Project:{reset}\n➡️  This Python program {r}directly supports{reset} SDG 8 by helping users—especially students and job seekers—explore career paths that match their{r} interests and strengths.{reset}\n➡️  By guiding people toward {r}suitable and fulfilling work{reset}, the program encourages informed career choices, increases {r}employability,{reset} and contributes to {r}long-term economic growth and decent employment.{reset}\n\n")
def instruction():
  print(f"{w}{underline}{bold}2.These are the instructions for the quiz:{reset}\n\n➡️  This quiz will ask you a {r}series of questions{reset} related to your personality and preferances\n➡️  For each question, 2 options will be given which you will have to choose and {r}submit{reset} as your answer for the specific question\n➡️  After you finish the quiz, you will be directed to a seperate page which{r} details{reset} of the best types of jobs for you!\n➡️  Enjoy!!\n\n{bold}-------------------------------------------------------------------------------{reset}\n")


#Ask user if they would like to start answering the questions
def start():
  start= input(f"{r}{bold}Would you like to start the quiz and find the job of your dreams? (y/n){reset}")
  if start.lower() == "y":
    os.system("clear")
    Q1()
  else:
    print(f"{bold}No problem! We hope to see you again when you're ready to find your dream jobs!{reset}")


#______________________________________________________________________________________________________________________________________#

#MAIN 
print(f"{bold}-------------------------Welcome to {bold}{r}'My Career Map'{reset}{bold}!----------------------------\n{reset}")
SDG_8()
connection()
instruction()
start()
