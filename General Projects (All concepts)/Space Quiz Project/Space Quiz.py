########################SPACE-QUIZ################

def planets_and_moons():
  correct = 0
  print("\n🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎")
  print("Welcome to the Planets and Moons Quiz!\nLet's get started!\n")

  # Question 1
  print("🌎--------Level: VERY EASY--------🌎")
  answer = input("Q1) How many planets are there in our solar system?\nA) 8\nB) 9\nC) 10\nD) 11\nEnter your answer: ")
  if answer.lower() == "a":
      print("\nCorrect!🌟✨💫⭐🌟🌠\nYou can move on to the next question!🌟✨💫⭐🌟🌠\n")
      correct += 1
  else:
      print("🚀🚀 Incorrect! The answer was A, 8.")

  # Question 2
  print("\n🌎--------Level: EASY--------🌎")
  answer = input("Q2) What's the name of the hottest planet in our solar system?\nA) Mercury\nB) Venus\nC) Earth\nD) Pluto\nEnter your answer: ")
  if answer.lower() == "b":
      print("\nCorrect!🌟✨💫⭐🌟🌠\nYou can move on to the next question!🌟✨💫⭐🌟🌠\n")
      correct += 1
  else:
      print("🚀🚀 Incorrect! The answer was B, Venus.")

  # Question 3
  print("\n🌎--------Level: MEDIUM--------🌎")
  answer = input("Q3) What's the name of the largest moon in our solar system, and which planet does it orbit?\nA) The Moon, Earth\nB) Titan, Saturn\nC) Ganymede, Jupiter\nD) Io, Jupiter\nEnter your answer: ")
  if answer.lower() == "c":
      print("\nCorrect!🌟✨💫⭐🌟🌠\nYou can move on to the next question!🌟✨💫⭐🌟🌠\n")
      correct += 1
  else:
      print("🚀🚀 Incorrect! The answer was C, Ganymede, Jupiter.")

  # Question 4
  print("\n🌎--------Level: HARD--------🌎")
  answer = input("Q4) What is the primary reason for the extreme temperature differences on Mercury?\n"
                 "A) The Sun's rays are blocked by Mercury's thick atmosphere\n"
                 "B) Its slow rotation and lack of atmosphere, causing one side to be extremely hot while the other is extremely cold.\n"
                 "C) It doesn't have a ring system to block the Sun's rays.\n"
                 "D) It's not a planet; it's a dwarf planet.\nEnter your answer: ")
  if answer.lower() == "b":
      print("\nCorrect!🌟✨💫⭐🌟🌠\nYou can move on to the next question!🌟✨💫⭐🌟🌠\n")
      correct += 1
  else:
      print("🚀🚀 Incorrect! The answer was B, Its slow rotation and lack of atmosphere.")

  # Question 5
  print("\n🌎--------Level: EXTREME--------🌎")
  answer = input("Q5) What is the role of the 'Roche Limit' in planetary ring systems?\n"
                 "A) It's a barrier that prevents planets from colliding with each other.\n"
                 "B) The Roche Limit is the distance within which a large body will be torn apart by tidal forces, contributing to the formation of planetary rings.\n"
                 "C) It is where a planet's gravitational field ends.\nEnter your answer: ")
  if answer.lower() == "b":
      print("\nCorrect!🌟✨💫⭐🌟🌠\nYou can move on to the next question!🌟✨💫⭐🌟🌠\n")
      correct += 1
  else:
      print("🚀🚀 Incorrect! The answer was B, The Roche Limit is the distance within which a large body will be torn apart by tidal forces.")

  # Final Results
  print("\n🚀 Quiz Completed!")
  print(f"You answered {correct} out of 5 questions correctly. 🌟✨💫⭐🌟")
  print("Thank you for playing! Come back soon! 🚀🚀")





#############################################################################################
def stars_and_galaxies():
  correct = 0
  print("\n🌌🌌🌌🌌🌌🌌🌌🌌🌌🌌🌌🌌🌌🌌🌌\nWelcome to the Stars and Galaxies Quiz!\nLet's get started!\n")

  # Question 1
  Q1 = input("🌌--------Level:VERY EASY--------🌌\nQ1) What Galaxy do we live in?\nA) The Andromeda Galaxy\nB) The Milky Way\nC) The Triangulum Galaxy\nD) The Whirlpool Galaxy\nEnter your answer: ")
  if Q1.lower() == "b":
      print("\nCorrect! 🌟✨💫⭐🌟🌠\n")
      correct += 1
  else:
      print("\n🚀🚀 Incorrect! The correct answer was B, The Milky Way.\n")

  # Question 2
  Q2 = input("🌌--------Level:EASY--------🌌\nQ2) What is a galaxy?\nA) A single star surrounded by planets\nB) A type of asteroid belt\nC) A glowing cloud of gas near Earth\nD) A massive system of stars, planets, dark matter etc.\nEnter your answer: ")
  if Q2.lower() == "d":
      print("\nCorrect! 🌟✨💫⭐🌟🌠\n")
      correct += 1
  else:
      print("\n🚀🚀 Incorrect! The correct answer was D, A massive system of stars, planets, dark matter etc.\n")

  # Question 3
  Q3 = input("🌌--------Level:MEDIUM--------🌌\nQ3) What is the primary difference between a star and a planet?\nA) Planets are brighter than stars\nB) A planet is very big compared to a star\nC) Stars emit their own light, while planets reflect the light of a star\nD) There is no difference\nEnter your answer: ")
  if Q3.lower() == "c":
      print("\nCorrect! 🌟✨💫⭐🌟🌠\n")
      correct += 1
  else:
      print("\n🚀🚀 Incorrect! The correct answer was C, Stars emit their own light, while planets reflect the light of a star.\n")

  # Question 4
  Q4 = input("🌌---------Level:HARD---------🌌\nQ4) What is a Supernova?\nA) A type of star that grows infinitely large\nB) The collision of two galaxies\nC) The formation of a black hole without any explosion\nD) An explosion that takes place when a star's core collapses\nEnter your answer: ")
  if Q4.lower() == "d":
      print("\nCorrect! 🌟✨💫⭐🌟🌠\n")
      correct += 1
  else:
      print("\n🚀🚀 Incorrect! The correct answer was D, An explosion that takes place when a star's core collapses.\n")

  # Question 5
  Q5 = input("🌌--------Level:EXTREME--------🌌\nQ5) Why do stars appear to twinkle when observed from Earth?\nA) Because the stars are rapidly moving further away from us\nB) It happens because of the Moon's gravitational pull\nC) Refraction takes place as the light from the stars passes through our atmosphere, causing it to appear as if it's twinkling\nEnter your answer: ")
  if Q5.lower() == "c":
      print("\nCorrect! 🌟✨💫⭐🌟🌠\n")
      correct += 1
  else:
      print("\n🚀🚀 Incorrect! The correct answer was C, Refraction takes place as the light from the stars passes through our atmosphere.\n")

  print(f"\nYou have completed the quiz! 🌌✨\nYou got {correct} out of 5 questions correct!")
#############################################################################################

def black_holes_and_space_phenomena():
  correct = 0
  print("\n☄️ Welcome to the Black Hole and Space Phenomena Quiz! ☄️\nLet's get started!\n")

  # Question 1
  Q1 = input("☄️--------Level: VERY EASY--------☄️\n"
             "Q1) What is a black hole?\n"
             "A) A type of star that emits no light.\n"
             "B) A hole in space created by an asteroid impact.\n"
             "C) A region of space where gravity is so strong that nothing, not even light, can escape it.\n"
             "D) A dark planet orbiting a distant star.\n"
             "Enter your answer: ").lower()
  if Q1 == "c":
      print("\nCorrect! 🌟✨💫\n")
      correct += 1
  else:
      print("\n🚀 Incorrect! The correct answer is C: A region of space where gravity is so strong that nothing, not even light, can escape it.\n")

  # Question 2
  Q2 = input("☄️--------Level: EASY--------☄️\n"
             "Q2) What is the Milky Way’s supermassive black hole called?\n"
             "A) Sagittarius A*\n"
             "B) Vega Core\n"
             "C) Sirius Alpha\n"
             "D) Andromeda Prime\n"
             "Enter your answer: ").lower()
  if Q2 == "a":
      print("\nCorrect! 🌟✨💫\n")
      correct += 1
  else:
      print("\n🚀 Incorrect! The correct answer is A: Sagittarius A*.\n")

  # Question 3
  Q3 = input("☄️--------Level: MEDIUM--------☄️\n"
             "Q3) What is a neutron star?\n"
             "A) A dense remnant of a massive star that has undergone a supernova, composed almost entirely of neutrons.\n"
             "B) A black hole that hasn’t fully formed.\n"
             "C) A young star in the early stages of formation.\n"
             "D) Planets are brighter than stars.\n"
             "Enter your answer: ").lower()
  if Q3 == "a":
      print("\nCorrect! 🌟✨💫\n")
      correct += 1
  else:
      print("\n🚀 Incorrect! The correct answer is A: A dense remnant of a massive star that has undergone a supernova, composed almost entirely of neutrons.\n")

  # Question 4
  Q4 = input("☄️--------Level: HARD--------☄️\n"
             "Q4) What is Hawking radiation?\n"
             "A) The light emitted by black holes.\n"
             "B) The gravitational waves created by merging black holes.\n"
             "C) The heat generated by neutron stars.\n"
             "D) Radiation emitted by black holes due to quantum effects near the event horizon.\n"
             "Enter your answer: ").lower()
  if Q4 == "d":
      print("\nCorrect! 🌟✨💫\n")
      correct += 1
  else:
      print("\n🚀 Incorrect! The correct answer is D: Radiation emitted by black holes due to quantum effects near the event horizon.\n")

  # Question 5
  Q5 = input("☄️--------Level: EXTREME--------☄️\n"
             "Q5) What is a quasar, and how is it related to black holes?\n"
             "A) A quasar is a collapsing black hole.\n"
             "B) A quasar is a small star orbiting a black hole.\n"
             "C) A highly energetic and luminous object powered by material falling into a supermassive black hole at the center of a galaxy.\n"
             "Enter your answer: ").lower()
  if Q5 == "c":
      print("\nCorrect! 🌟✨💫\nYou have completed the quiz!\n")
      correct += 1
  else:
      print("\n🚀 Incorrect! The correct answer is C: A highly energetic and luminous object powered by material falling into a supermassive black hole at the center of a galaxy.\n")

  # Final Score
  print("You got {correct} out of 5 questions correct! 🚀\nThanks for playing!\n")

#############################################################################################
def space_exploration_and_missions():
    correct = 0
    print("\n🛰️ Welcome to the Space Explorations and Missions Quiz! 🛰️\nLet's get started!\n")

    # Question 1
    Q1 = input("🛰️📡--------Level: VERY EASY--------📡🛰️\n"
               "Q1) Who was the first person to walk on the Moon?\n"
               "A) Yuri Gagarin\n"
               "B) Michael Collins\n"
               "C) Neil Armstrong\n"
               "D) Buzz Aldrin\n"
               "Enter your answer: ")
    if Q1.lower() == "c":
        print("\nCorrect! 🌟✨💫\n")
        correct += 1
    else:
        print("\n🚀 Incorrect! The correct answer is C: Neil Armstrong.\n")

    # Question 2
    Q2 = input("🛰️📡--------Level: EASY--------📡🛰️\n"
               "Q2) What was the first artificial satellite launched into space?\n"
               "A) Sputnik 1\n"
               "B) Apollo 11\n"
               "C) Hubble Space Telescope\n"
               "D) Voyager 1\n"
               "Enter your answer: ")
    if Q2.lower() == "a":
        print("\nCorrect! 🌟✨💫\n")
        correct += 1
    else:
        print("\n🚀 Incorrect! The correct answer is A: Sputnik 1.\n")

    # Question 3
    Q3 = input("🛰️📡--------Level: MEDIUM--------📡🛰️\n"
               "Q3) What is the Hubble Space Telescope?\n"
               "A) An orbiting observatory that captures detailed images of distant galaxies, stars, etc.\n"
               "B) A probe that landed on Mars\n"
               "C) A satellite that monitors Earth’s weather\n"
               "D) A communication device for the ISS\n"
               "Enter your answer: ")
    if Q3.lower() == "a":
        print("\nCorrect! 🌟✨💫\n")
        correct += 1
    else:
        print("\n🚀 Incorrect! The correct answer is A: An orbiting observatory that captures detailed images of distant galaxies, stars, etc.\n")

    # Question 4
    Q4 = input("🛰️📡--------Level: HARD--------📡🛰️\n"
               "Q4) What is the significance of the James Webb Space Telescope (JWST)?\n"
               "A) It replaces the Hubble Telescope for observing Earth\n"
               "B) It detects black holes using radio signals\n"
               "C) It is a probe sent to study the asteroid belt\n"
               "D) Observes the universe in infrared, allowing scientists to study the formation of stars, galaxies, and exoplanets\n"
               "Enter your answer: ")
    if Q4.lower() == "d":
        print("\nCorrect! 🌟✨💫\n")
        correct += 1
    else:
        print("\n🚀 Incorrect! The correct answer is D: Observes the universe in infrared, allowing scientists to study the formation of stars, galaxies, and exoplanets.\n")

    # Question 5
    Q5 = input("🛰️📡--------Level: EXTREME--------📡🛰️\n"
               "Q5) Why is studying Mars important for future space exploration?\n"
               "A) Mars is one of Earth's natural satellites\n"
               "B) Mars is the only planet that could support Earth-like wildlife\n"
               "C) It helps us understand planetary evolution and assess the planet's habitability\n"
               "D) Mars has been found to contain oceans of liquid water\n"
               "Enter your answer: ")
    if Q5.lower() == "c":
        print("\nCorrect! 🌟✨💫\nYou have completed the quiz!\n")
        correct += 1
    else:
        print("\n🚀 Incorrect! The correct answer is C: It helps us understand planetary evolution and assess the planet's habitability.\n")

    # Final Score
    print("You got ",correct," out of 5 questions correct! 🚀\nThanks for playing!\n")

    #end 1
#############################################################################################


def choice():
  print("\nChoose your cosmic challenge:")
  print("1. Planets and Moons 🌍🌑")
  print("2. Stars and Galaxies ✨🌌")
  print("3. Black Holes and Space Phenomena 🕳️🌀")
  print("4. Space Exploration and Missions 🛰️🚀")
  choice=int(input("Enter your choice here:"))
  if choice==1:
    planets_and_moons()
  elif choice==2:
    stars_and_galaxies()
  elif choice==3:
    black_holes_and_space_phenomena()
  elif choice==4:
    space_exploration_and_missions()
  else:
    print("Invalid choice. Please try again.")



def space_quiz_intro():
  print("🌌 Welcome to the Ultimate Space Quiz! 🚀")
  print("Are you ready to embark on a journey across the stars?")
  print("In this quiz, you'll test your knowledge about the mysteries of space!")
  print("\nAre you ready to take on the challenge and prove your space knowledge?")
  play=input("Enter 'yes' to begin or 'no' to exit: ")
  if play.lower()=="yes":
    print("\nGreat! Let's get started.")
    choice()
  else:
    print("\nMaybe next time. Goodbye!")

space_quiz_intro()
