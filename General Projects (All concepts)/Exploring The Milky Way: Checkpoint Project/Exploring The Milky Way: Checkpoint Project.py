#Title:Exploring the Milky Way
#Theme:Travelling on  a rocket shipe and exploring the milky way.
#Items to buy:Rocket Feul,foods,water,space suits,space helmet,space goggles,space binoculars,space camera
#Currency:Space pounds
quantity=0
total_spent=0
rocket_fuel = 100
food = 50
water = 40
space_suits = 150
space_helmet = 200
space_goggles=120
space_binoculars=250
space_camera=300
print("Welcome to your mission around the Milky Way!\n\nThe Milky Way Galaxy is a huge collection of stars, dust, and gas.It is home to an estimated 100 billion stars\nand it is where we, Humans live!\n")
home=input("Would you like to explore the milky way?🚀\n")
home=home.lower()
if home== "yes":
  print("Great! Lets get started!\n")
  print("You have left Earth and you are about 10 light years away from home!You suddenly realise that you might need to buy some supplies for your journey in space.🌎🛰️🌌\n")
  while True:
    print("What would you like to buy?\n\n1.Rocket fuel:100 space pounds\n2.Food:50 space pounds\n3.Water:40 space pounds\n4.Space suits:150 space pounds\n5.Space helmet:200 space pounds\n6.Space goggles:120 space pounds\n7.Space binoculars:250 space\n8.Space camera:300 space pounds\nq.Quit\n")
    choice = input("\n🛰️🌎🚀🌌Enter your choice here:")
    choice=choice.lower()
    if choice == "1" or choice=="rocket fuel":
      amount=input("How much would you like to buy of this item?")
      if amount.isalpha():
        print("Invalid amount.Please enter a number.")
      else:
        cost=int(amount)*100
        total_spent=total_spent+cost
        print("Buying Rocket fuel....\nYou have spent",total_spent,"space pounds so far...\n\n")
    elif choice == "2" or choice=="food":
      amount=input("How much would you like to buy of this item?")
      if amount.isalpha():
        print("Invalid amount.Please enter a number.")
      else:
        cost=int(amount)*50
        total_spent=total_spent+cost
        quantity=quantity+int(amount)
        print("Buying Food....\nYou have spent",total_spent,"space pounds so far...\n\n")
    elif choice == "3" or choice=="water":
      amount=input("How much would you like to buy of this item?")
      if amount.isalpha():
        print("Invalid amount.Please enter a number.")
      else:
        cost=int(amount)*40
        total_spent=total_spent+cost
        quantity=quantity+int(amount)
        print("Buying Water....\nYou have spent",total_spent,"space pounds so far...\n")
    elif choice == "4" or choice=="space suit":
      amount=input("How much would you like to buy of this item?")
      if amount.isalpha():
        print("Invalid amount.Please enter a number.")
      else:
        cost=int(amount)*150
        total_spent=total_spent+cost
        quantity=quantity+int(amount)
        print("Buying Space suits....\nYou have spent",total_spent,"space pounds so far...\n")
    elif choice=="5" or choice=="space helmet":
      amount=input("How much would you like to buy of this item?")
      if amount.isalpha():
        print("Invalid amount.Please enter a number.")
      else:
        cost=int(amount)*200
        total_spent=total_spent+cost
        quantity=quantity+int(amount)
        print("Buying Space helmet....\nYou have spent",total_spent,"space pounds so far...\n")
    elif choice=="6" or choice=="space goggles":
      amount=input("How much would you like to buy of this item?")
      if amount.isalpha():
        print("Invalid amount.Please enter a number.")
      else:
        cost=int(amount)*120
        total_spent=total_spent+cost
        quantity=quantity+int(amount)
        print("Buying Space goggles....\nYou have spent",total_spent,"space pounds so far...\n")
    elif choice=="7" or choice=="space binoculars":
      amount=input("How much would you like to buy of this item?")
      if amount.isalpha():
        print("Invalid amount.Please enter a number.")
      else:
        cost=int(amount)*250
        total_spent=total_spent+cost
        quantity=quantity+int(amount)
        print("Buying Space binoculars....\nYou have spent",total_spent,"space pounds so far...\n")
    elif choice=="8" or choice=="space camera":
      amount=input("How much would you like to buy of this item?")
      if amount.isalpha():
        print("Invalid amount.Please enter a number.")
      else:
        cost=int(amount)*300
        total_spent=total_spent+cost
        quantity=quantity+int(amount)
        print("Buying Space camera....\nYou have spent",total_spent,"space pounds so far...\n")
    elif choice=="q" or choice=="quit":
      print("\nThank you for travelling and exploring the milky way!\n\nYou have spent a total of",total_spent,"space pounds\nYou have bought",quantity,"items\nHope you had a great time shopping!")
      break
    else:
      print("Invalid choice. Please try again.\n")
else:
  print("\nOkay, maybe next time!\nI hope to see you soon!")  
