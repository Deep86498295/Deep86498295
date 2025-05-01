import random
num=random.randint(1,100)
for i in range(100):
  log=int(input("What is the number?"))
  if num==log: 
    print("You gussed the right number.")
    break 
  elif num!= log:
    if num>log:
      print ("This is too small! Try again with bigger number.")
    elif num<log:
      print ("This is too big ! Try again with a smaller number.")