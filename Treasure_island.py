print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#ask for a direction
d1 = input("Which way do you want to go? enter: l = left or r = right. \n").lower()
if d1 == "l":
  print("You have made it to the edge of the water")
#ask for swim or wait for a boat
  d2 = input("Do you want to swim to the island or wait for a boat? enter: s = swim, w = wait \n").lower()
  if d2 == "w":
    print("You made it to the island safely")
    print("You see 3 doors, their colors are red, yellow, and blue")
#ask to pick a door
    d3 = input("Which door do you choose? enter: r = red, y = yellow, or b = blue \n").lower()
    if d3 == "y":
      print("Congratulations! You have found the treasure!!!")
    elif d3 == "r":
      print("Game Over! You were hit by a falling anvil!")
    elif d3 == "b":
      print("Game Over! There was a hungry lion behind the door!")
    else:
      print("Game Over! You failed to enter a valid response! You fell into a pit of poisonous snakes and died!")
  elif d2 == "s":
    print("Game Over! You were eaten by a shark!")
  else:
    print("Game Over! You failed to enter a valid response! You were eaten by monster ants!")
elif d1 == "r":
  print("Game Over! You fell off a cliff!")
else:
  print("Game Over! You failed to enter a valid response! You were sucked up by a hurricane!")
