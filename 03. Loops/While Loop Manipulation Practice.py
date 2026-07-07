Iron = 2000
Gold=5000
Platinum=10000
total=0
quantity=0
print("WELCOME TO ROCKETMINE\nUse your OreBucks (Ø) to buy different types of rockets!\n")
while True:
  print("1. Iron Ore\t 2000\n2. Gold Ore\t5000\n3. Platinum Ore\t10000\n4. q to quit")
  print("Current Total:",total)
  choice=input("Enter your choice: ")
  if choice =="1":
    quantity=int(input("Enter the quantity: "))
    total=total+(Iron*quantity)
    print("Buying Iron ore:...\n",(Iron*quantity))
    print("Your total is: ",total,"\n")
    quantity=quantity+quantity
  elif choice =="2":
    quantity=int(input("Enter the quantity: "))
    total=total+(Gold*quantity)
    print("Buying Gold ore...\n",(Gold*quantity))
    print("Your total is: ",total,"\n")
    quantity=quantity+quantity
  elif choice =="3":
    quantity=int(input("Enter the quantity: "))
    total=total+(Platinum*quantity)
    print("Buying Platinum ore...\n",(Platinum*quantity))
    print("Your total is: ",total,"\n")
    quantity=quantity+quantity
  elif choice =="q":
    print("Total:",total)
    print("Total quantity:",quantity)
    break
  else:
    print("Invalid Choice\n")

