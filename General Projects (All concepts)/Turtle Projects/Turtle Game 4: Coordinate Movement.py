x = 0
y = 0
while True:
  print("Your current poistion is:","(",x,",",y,")")
  num_x = int(input("Enter your x coordinate:"))
  num_y = int(input("Enter your y coordinate:"))
  if num_x==0 and num_y==0:
    break
  else:
    x = x + num_x
    y = y + num_y
print("NO MOVEMENT DETECTED\nExiting.....\nFinal position is:","(",x,",",y,")")
