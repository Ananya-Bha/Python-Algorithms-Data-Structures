#################SCIENCE-QUIZ################################

#Biology Quiz############################################################
def biology():
    correct=0
    print("Welcome to the Biology Quiz!")
    print("Answer the following questions to test your knowledge.")
    print("You will be given 4 options for each question.")
    print("Choose the correct option by typing the corresponding letter.")
    print("Let's begin!\n")
    print("🧫🧬🧫🧬🧫🧬🧫🧬🧫🧬🧫🧬🧫🧬🧫🧬🧫🧬🧫🧬🧫🧬🧫🧬")
    #Question 1
    Q1=input("----------Level:EASY----------\nQuestion 1: What is the basic unit of life?\nA. Cell\nB. Atom\nC. Molecule\nD. Organism\n Enter your answer here:")
    if Q1.lower()=="a":
        print("\nCorrect!🌟✨💫You can move on to the next question!\n")
        correct=correct+1
    else:
        print("\nIncorrect! The correct answer was A. Cell.🚀\n")
    #Question 2
    Q2=input("----------Level:Medium-----------\nQuestion 2:Which organelle is known as the powerhouse of the cell? \nA.Ribosome \nB. Nucleus\nC. Mitochondria\nD. Golgi Apparatus\n Enter your answer here:")
    if Q2.lower()=="c":
        print("\nCorrect!🌟✨💫You can move on to the next question!\n")
        correct=correct+1
    else:
        print("\nIncorrect! The correct answer was C. Mitochondria.🚀\n")
    #Question 3
    Q3=input("Level:Hard\nQuestion 3: What is the primary function of the lymphatic system in the human body?\nA) To circulate oxygen-rich blood to tissues.\nB) To produce energy for muscle contraction.\nC) To defend the body against infections and maintain fluid balance.\nD) To deliver hormones to target organs.\n Enter your answer here:")
    if Q3.lower()=="c":
        print("\nCorrect!🌟✨💫You can move on to the next question!\n")
        correct=correct+1
    else:
        print("\nIncorrect! The correct answer was C. To defend the body against infections and maintain fluid balance")
    #Question 4
    Q4=input("----------Level:Extreme----------\nQuestion 4:What farm machine is used to separates the edible part of a grain from the straw or chaff of crops like wheat, peas, soybeans, and other small grains?\nA.Saw\nB.Sieve\nC.Slicer\nD.Thresher\n Enter your answer here:")
    if Q4.lower()=="d":
        correct=correct+1
        print("\nCorrect!🌟✨💫You have completed the Quiz!\n You have gotten",correct,"out of 4 questions correct!")

    else:
        print("\nIncorrect! The correct answer was D. Thresher.🚀\nThe Quiz is over!\nYou got", correct, "out of 4 questions correct!\n")


#Chemistry Quiz##########################################################

def chemistry():
    correct=0
    print("Welcome to the Chemistry Quiz!")
    print("Answer the following questions to test your knowledge.")
    print("You will be given 4 options for each question.")
    print("Choose the correct option by typing the corresponding letter.")
    print("Let's begin!\n")
    print("🔬🧪⚗️🔬🧪⚗️🔬🧪⚗️🔬🧪⚗️🔬🧪⚗️🔬🧪⚗️🔬🧪⚗️🔬🧪⚗️")
    #Question 1
    Q1=input("----------Level:EASY----------\nQuestion 1: What is the chemical formula for water?\nA) H2O\nB) CO2\nC) O2\nD) H2O2\nEnter you choice her:")
    if Q1.lower()=="a":
        print("\nCorrect!🌟✨💫You can move on to the next question!\n")
        correct=correct+1
    else:
        print("\nIncorrect! The correct answer was A,H20🚀\n")
    #Question 2
    Q2=input("----------Level:Medium-----------\nQuestion 2:What is the pH level of a neutral solution?\nA) 1\nB) 7\nC) 14\nEnter your answer here:")
    if Q2.lower()=="b":
        print("\nCorrect!🌟✨💫You can move on to the next question!\n")
        correct=correct+1
    else:
        print("\nIncorrect! The correct answer was B. 7 pH.🚀\n")
    #Question 3
    Q3=input("Level:Hard\nQuestion 3:What is electronegativity?\nA) The ability of an atom to lose electrons and form a cation.\nB) The ability of an atom to gain protons during a chemical reaction.\nC) The tendency of an atom to attract electrons towards itself in a chemical bond.\nD) The measure of the energy required to remove an electron from an atom.\nEnter your answer here:")
    if Q3.lower()=="c":
        print("\nCorrect!🌟✨💫You can move on to the next question!\n")
        correct=correct+1
    else:
        print("\nIncorrect! The correct answer was C. The tendency of an atom to attract electrons towards itself in a chemical bond.\n")
    #Question 4
    Q4=input("----------Level:Extreme----------\nQuestion 4:Which of the following elements has the highest electronegativity?\nA.Sodium (Na)\nB.Fluorine (F)\nC.Oxygen (O)\nD.Chlorine (Cl)\nEnter your answer here:")
    if Q4.lower()=="b":
        correct=correct+1
        print("\nCorrect!🌟✨💫You have completed the Quiz!\n You have gotten",correct,"out of 4 questions correct!\n")

    else:
        print("\nIncorrect! The correct answer was B.Flourine.🚀\nThe Quiz is over!\nYou got", correct, "out of 4 questions correct!\n")


#Physics Quiz##########################################################
def physics():
    correct=0
    print("Welcome to the Physics Quiz!")
    print("Answer the following questions to test your knowledge.")
    print("You will be given 4 options for each question.")
    print("Choose the correct option by typing the corresponding letter.")
    print("Let's begin!\n")
    print("👨‍🔬🔭👨‍🔬🔭👨‍🔬🔭👨‍🔬🔭👨‍🔬🔭👨‍🔬🔭👨‍🔬🔭👨‍🔬🔭👨‍🔬🔭👨‍🔬🔭👨‍🔬🔭👨‍🔬🔭👨‍🔬🔭")
    #Question 1
    Q1=input("----------Level:EASY----------\nQuestion 1: What is the primary unit of force in the International System of Units (SI)?\nA)Joule\nB)Watt\nC)Newton\nD)Pascal\nEnter your choice here:")
    if Q1.lower()=="c":
        print("\nCorrect!🌟✨💫You can move on to the next question!\n")
        correct=correct+1
    else:
        print("\nIncorrect! The correct answer was c,Newtons🚀\n")
    #Question 2
    Q2=input("----------Level:Medium-----------\nQuestion 2:Why does light bend when it passes from air into water?\nA)The speed of light increases in water, causing refraction.\nB)Light bends due to the gravitational pull of water molecules.\nC)The speed of light decreases in water, causing refraction.\n Enter your choice Here:")
    if Q2.lower()=="c":
        print("\nCorrect!🌟✨💫You can move on to the next question!\n")
        correct=correct+1
    else:
        print("\nIncorrect! The correct answer was C,The speed of light decreases in water, causing refraction.🚀\n")
    #Question 3
    Q3=input("Level:Hard\nQuestion 3:What happens to the gravitational force between two objects if the distance between them is doubled?\nA) It becomes twice as strong.\nB) It becomes four times as strong.\nC) It becomes half as strong.\nD)  It becomes one-fourth as strong.\n Enter your answer here:")
    if Q3.lower()=="d":
        print("\nCorrect!🌟✨💫You can move on to the next question!\n")
        correct=correct+1
    else:
        print("\nIncorrect! The correct answer was D, It becomes one-fourth as strong.\n")
    #Question 4
    Q4=input("----------Level:Extreme----------\nQuestion 4:What happens to the frequency of a wave as its wavelength decreases (assuming constant wave speed)?\nA.Frequency decreases. \nB.Frequency increases.\nC.Frequency remains constant.\nD.Frequency becomes zero.\n Enter your answer here:")
    if Q4.lower()=="b":
        correct=correct+1
        print("\nCorrect!🌟✨💫You have completed the Quiz!\n You have gotten",correct,"out of 4 questions correct!\n")

    else:
        print("\nIncorrect! The correct answer was B.Frequency increases.🚀\nThe Quiz is over!\nYou got", correct, "out of 4 questions correct!\n")

#Choice##################################################################
def choice():
  print("\nChoose the Subject that you want to challenge:")
  print("1. Biology🧫🧬")
  print("2. Chemistry🔬🧪⚗️")
  print("3. Physics👨‍🔬🔭")
  choice=int(input("Enter your choice here:"))
  if choice==1:
    biology()
  elif choice==2:
    chemistry()
  elif choice==3:
    physics()
  else:
    print("Invalid choice. Please try again.")


def science_quiz_intro():
  print("🌌 Welcome to the Ultimate Science Quiz! 🚀")
  print("Are you ready to embark on a journey and explore the wonders of Science?")
  print("In this quiz, you'll test your knowledge about you scientific knowledge!\n(PS:This quiz has questions from the science olympiad!)")
  print("\nAre you ready to take on the challenge and prove your space knowledge?")
  play=input("Enter 'yes' to begin or 'no' to exit: ")
  if play.lower()=="yes":
    print("\nGreat! Let's get started.")
    choice()
  else:
    print("\nMaybe next time. Goodbye!")
science_quiz_intro()
